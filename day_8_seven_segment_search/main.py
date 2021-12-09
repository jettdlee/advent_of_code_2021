import pdb
import numpy as np
from helpers.import_data import ImportData

class SegmentDigits:
    def __init__(self):
        self.segment_counts = { 0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6 } 

    def getMappingFromSegments(self, segments):
        mapping = {}
        for segment in segments:
            ordered_segment = self.orderSegment(segment)
            if len(segment) == 2:
                mapping[1] = ordered_segment
            elif len(segment) == 4: 
                mapping[4] = ordered_segment
            elif len(segment) == 3: 
                mapping[7] = ordered_segment
            elif len(segment) == 7: 
                mapping[8] = ordered_segment
            else:
                continue

        top_left_and_middle_segments = self.__stripCharactersFromString(mapping[1], mapping[4])
        for segment in segments:
            ordered_segment = self.orderSegment(segment)
            if len(segment) == 5:
                if self.__checkAllStringInSegment(top_left_and_middle_segments, ordered_segment):
                    mapping[5] = ordered_segment
                elif self.__checkAllStringInSegment(mapping[1], ordered_segment):
                    mapping[3] = ordered_segment
                else:
                    mapping[2] = ordered_segment

        for segment in segments:
            ordered_segment = self.orderSegment(segment)
            if len(segment) == 6:
                if not self.__checkAllStringInSegment(top_left_and_middle_segments, ordered_segment):
                    mapping[0] = ordered_segment
                elif self.__checkAllStringInSegment(mapping[1], ordered_segment):
                    mapping[9] = ordered_segment
                else:
                    mapping[6] = ordered_segment

        return { v: k for k, v in mapping.items()}
    
    def orderSegment(self, segment):
        return ''.join(sorted(segment))

    def __stripCharactersFromString(self, remove, target):
        new_target = target
        for char in remove:
            new_target = new_target.replace(char, '')
        return ''.join(new_target)
    
    def __checkAllStringInSegment(self, string, segment):
        string_to_check = string
        for char in string:
            if char in segment:
                string_to_check = string_to_check.replace(char, '')
        return len(string_to_check) == 0
        
class SegmentParser:
    def __init__(self, dataset):
        self.dataset = dataset
        self.__splitSegments()

    def __splitSegments(self):
        self.signals = []
        for row in self.dataset:
            signal = []
            left_signal, right_signal = row.split(' | ')
            segments_pattern = left_signal.split(' ')
            output_pattern = right_signal.split(' ')
            self.signals.append({ 'segments': segments_pattern, 'outputs': output_pattern })
    
class SignalReader:
    def __init__(self, segment_parser, segment_digits=SegmentDigits()):
        self.signals = segment_parser.signals
        self.segment_digits = segment_digits

    def countUniqueOutputs(self, digits_to_check):
        count = 0
        segment_counts_for_digits = self.__getSegmentCounts(digits_to_check)

        for signal in self.signals:
            outputs = signal['outputs']
            for output in outputs:
                if len(output) in segment_counts_for_digits:
                    count += 1
        print('Count of unique digits: ', count)

    def decodeOutputsFromSegments(self):
        sum = 0
        for signal in self.signals:
            entry = []
            segments = signal['segments']
            outputs = signal['outputs']
            mapping = self.segment_digits.getMappingFromSegments(segments)
            for output in outputs:
                order_output = self.segment_digits.orderSegment(output)
                entry.append(mapping[order_output])
            sum += int(''.join(map(str, entry)))

        print('Sum of decoded sigits:', sum)

    def __getSegmentCounts(self, digits_to_check):
        segment_counts = []
        for digit in digits_to_check:
            segment_counts.append(self.segment_digits.segment_counts[digit])
        return segment_counts


if __name__ == "__main__":
    data_file = ImportData('day_8.data')
    segment_parser = SegmentParser(data_file.dataset)
    signal_reader = SignalReader(segment_parser)
    signal_reader.countUniqueOutputs([1, 4, 7, 8])
    signal_reader.decodeOutputsFromSegments()

