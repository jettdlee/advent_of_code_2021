import pdb
import numpy as np
from helpers.import_data import ImportData

class Sensor:
    def __init__(self, dataset):
        self.dataset = dataset
        self.cave_map = self.__constructMap()

    def getAllRoutes(self):
        all_routes_found = False
        finished_routes = []
        current_route = ['start']
        self.getPosition('start', [])

    def getPosition(self, current_position, current_route):
        if current_position == 'end':
            finished_route.append(current_route.copy())
        else:
            for neighbour in self.cave_map[current_position]:
                if not(neighbour in current_route and neighbour.islower()):
                    self.getPosition(neighbour, current_route)

        current_route.pop()


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
    data_file = ImportData('test3.data')
    sensor = Sensor(data_file.dataset)
    sensor.getAllRoutes()
