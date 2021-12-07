import pdb
import numpy as np
from helpers.import_data import ImportData

class CrabFuel:
    def __init__(self, dataset):
        self.dataset = dataset
        self.crabs = self.__setupCrabs()
        self.min_position = min(self.crabs)
        self.max_position = max(self.crabs)

    def run(self):
        fuel_cost_dict = {}
        fuel_array = []
        for position in range(self.min_position, self.max_position+1):
            fuel_cost = 0
            for crab in self.crabs:
                fuel_cost += abs(crab - position)
            # fuel_cost_dict[position] = fuel_cost
            fuel_array.append(fuel_cost)
        print(min(fuel_array))

    def __setupCrabs(self):
        return list(map(int, self.dataset[0].split(',')))

if __name__ == "__main__":
    data_file = ImportData('day_7.data')
    crab_fuel = CrabFuel(data_file.dataset)
    crab_fuel.run()
