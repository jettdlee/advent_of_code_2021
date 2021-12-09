import pdb
import numpy as np
from helpers.import_data import ImportData

class HeightMap:
    def __init__(self, dataset):
        self.dataset = dataset
        self.__setupHeightMap()
        self.row_len = len(self.dataset[0]) - 1

    def findLowPoints(self):
        low_points = []
        for x_axis, height_map_row in enumerate(self.height_map):
            for y_axis, point in enumerate(height_map_row):
                if self.__lowestInAdjacentPoints(point, x_axis, y_axis):
                    low_points.append(point)
        return low_points
    
    def calculateRiskLevel(self, low_points):
        sum = 0
        for point in low_points:
            sum += 1 + point
        print('Sum of Risk level: ', sum)

    def __setupHeightMap(self):
        self.height_map = []
        for row in self.dataset:
            row_array = [int(point) for point in row]
            self.height_map.append(row_array)

    def __lowestInAdjacentPoints(self, point, x_axis, y_axis):
        all_points = [point]
        if not x_axis == 0:
            all_points.append(self.height_map[x_axis - 1][y_axis])
        if not x_axis == self.row_len:
            all_points.append(self.height_map[x_axis + 1][y_axis])
        if not y_axis == 0:
            all_points.append(self.height_map[x_axis][y_axis - 1])
        if not y_axis == self.row_len:
            all_points.append(self.height_map[x_axis][y_axis + 1])
        return point == min(all_points) and all_points.count(point) == 1

if __name__ == "__main__":
    data_file = ImportData('day_9.data')
    height_map = HeightMap(data_file.dataset)
    low_points = height_map.findLowPoints()
    print('Low Points: ', low_points)
    height_map.calculateRiskLevel(low_points)
