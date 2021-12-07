import pdb
import numpy as np
from helpers.import_data import ImportData


class HydrothermalParser:
    def __init__(self, dataset):
        self.dataset = dataset
        self.ranges = []
        self.__parse()

    def __parse(self):
        for row in self.dataset:
            start, end = row.split(' -> ')
            start_position = start.split(',')
            end_position = end.split(',')
            line = [{'x': int(start_position[0]), 'y': int(start_position[1])}, {'x': int(end_position[0]), 'y': int(end_position[1])}]
            self.ranges.append(line)
            
class HydrothermalMap:
    def __init__(self, parser, map_size=1000):
        self.coordinates = parser.ranges
        self.map_size = map_size
        self.__instantiateMap()

    def plotLines(self):
        for line in self.coordinates:
            if self.__is_line_diagonal(line):
                continue
            self.__plotOnMap(line)

    def countOverlap(self):
        count = 0
        for row in self.hydrothermal_map:
            count += len(np.where(np.array(row) > 1)[0])
        print(count)

    def __instantiateMap(self):
        self.hydrothermal_map = []
        for i in range(self.map_size):
            self.hydrothermal_map.append([0] * self.map_size)
            
    def __is_line_diagonal(self, line):
        return line[0]['x'] != line[1]['x'] and line[0]['y'] != line[1]['y']

    def __plotOnMap(self, line):
        start_position = line[0]
        end_position = line[1]
        if start_position['x'] == end_position['x']:
            x_axis = start_position['x']
            increment = self.__getIncrement(start_position['y'], end_position['y'])
            for y_axis in range(start_position['y'], end_position['y'] + increment, increment):
                self.hydrothermal_map[x_axis][y_axis] += 1
        else:
            y_axis = start_position['y']
            increment = self.__getIncrement(start_position['x'], end_position['x'])
            for x_axis in range(start_position['x'], end_position['x'] + increment, increment):
                self.hydrothermal_map[x_axis][y_axis] += 1

    def __getIncrement(self, start, end):
        if start > end:
            return -1
        else:
            return 1

if __name__ == "__main__":
    data_file = ImportData('day5.data')
    parser = HydrothermalParser(data_file.dataset)
    hydro_map = HydrothermalMap(parser)
    hydro_map.plotLines()
    hydro_map.countOverlap()
