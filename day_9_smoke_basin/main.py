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
        positions = []
        for x_axis, height_map_row in enumerate(self.height_map):
            for y_axis, point in enumerate(height_map_row):
                if self.__lowestInAdjacentPoints(point, x_axis, y_axis):
                    low_points.append(point)
                    positions.append([x_axis, y_axis])
        return low_points, positions
    
    def calculateRiskLevel(self, low_points):
        sum = 0
        for point in low_points:
            sum += 1 + point
        print('Sum of Risk level: ', sum)

    def findBasinSizes(self, positions):
        basin_sizes = []
        for position in positions:
            point = self.height_map[0][1]
            if point == 9:
                continue

            basin_positions = [position]
            all_positions_checked = False
            while all_positions_checked == False: 
                all_positions_checked = True
                for basin_position in basin_positions:
                    adjacent_points, positions = self.__getPointsAndPositionsAdjacentToLocation(basin_position[0], basin_position[1])
                    for index in range(len(adjacent_points)):
                        if not adjacent_points[index] == 9 and positions[index] not in basin_positions:
                            all_positions_checked = False
                            basin_positions.append(positions[index])

            basin_sizes.append(len(basin_positions))
        return basin_sizes
            
    def __setupHeightMap(self):
        self.height_map = []
        for row in self.dataset:
            row_array = [int(point) for point in row]
            self.height_map.append(row_array)

    def __lowestInAdjacentPoints(self, point, x_axis, y_axis):
        adjacent_points, _ = self.__getPointsAndPositionsAdjacentToLocation(x_axis, y_axis)
        all_points = [point] + adjacent_points
        return point == min(all_points) and all_points.count(point) == 1
    
    def __getPointsAndPositionsAdjacentToLocation(self, x_axis, y_axis):
        points = []
        positions = []
        if not x_axis == 0:
            positions.append([x_axis - 1, y_axis])
            points.append(self.height_map[x_axis - 1][y_axis])
        if not x_axis == self.row_len:
            positions.append([x_axis + 1, y_axis])
            points.append(self.height_map[x_axis + 1][y_axis])
        if not y_axis == 0:
            positions.append([x_axis, y_axis - 1])
            points.append(self.height_map[x_axis][y_axis - 1])
        if not y_axis == self.row_len:
            positions.append([x_axis, y_axis + 1])
            points.append(self.height_map[x_axis][y_axis + 1])

        return points, positions


if __name__ == "__main__":
    data_file = ImportData('day_9.data')
    height_map = HeightMap(data_file.dataset)
    low_points, positions = height_map.findLowPoints()
    print('Low Points: ', low_points)
    height_map.calculateRiskLevel(low_points)
    basin_sizes = height_map.findBasinSizes(positions)
    basin_sizes.sort()
    result = 1
    for i in basin_sizes[-3:]:
        result = result * i
    print('Basin Sizes: ', basin_sizes)
    print('Product of top 3: ', result)
