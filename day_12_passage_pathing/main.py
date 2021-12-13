import pdb
import numpy as np
from helpers.import_data import ImportData

class Sensor:
    def __init__(self, dataset):
        self.dataset = dataset
        self.cave_map = self.__constructMap()

    def getAllPaths(self):
        all_paths_found = False
        paths = []
        while all_paths_found == False:
            position = 'start'







    def __constructMap(self):
        map_dict = {}
        for row in self.dataset:
            point1, point2 = row.split('-')
            map_dict = self.__addPointToMap(map_dict, point1, point2)
            map_dict = self.__addPointToMap(map_dict, point2, point1)
        return map_dict

    def __addPointToMap(self, map_dict, a, b):
        if a not in map_dict:
            map_dict[a] = []
        map_dict[a].append(b)
        return map_dict

if __name__ == "__main__":
    data_file = ImportData('test1.data')
    sensor = Sensor(data_file.dataset)
