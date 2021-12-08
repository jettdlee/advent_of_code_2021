import pdb
import numpy as np
from helpers.import_data import ImportData

class SegmentDigits:
    def __init__(self):
        self.segment_counts = { 0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6 } 

class SegmentParser:
    def __init__(self, dataset):
        self.dataset = dataset
        self.__splitSegments()

    def __splitSegments(self):
        self.signals = []
        for row in self.dataset:
            signal = []
            left_signal, right_signal = row.split(' | ')
            signal_pattern = left_signal.split(' ')
            output_pattern = right_signal.split(' ')
            self.signals.append({ 'signals': signal_pattern, 'outputs': output_pattern })
    
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
        print(count)

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

