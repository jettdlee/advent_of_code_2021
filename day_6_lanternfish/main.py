import pdb
import numpy as np
from helpers.import_data import ImportData


class LanternFish():
    def __init__(self, lifespan=8):
        self.lifespan = lifespan

    def decrementDay(self):
        if self.lifespan == 0:
            self.lifespan = 6
            return LanternFish()
        else:
            self.lifespan -= 1

class FishCounter:
    def __init__(self, dataset):
        self.dataset = list(map(int, dataset[0].split(',')))

    def countFish(self, days):
        fish_array = []
        for lifespan in self.dataset:
            fish_array.append(LanternFish(lifespan))

        for day in range(days):
            for fish in fish_array:
                new_fish = fish.decrementDay()
                if new_fish is not None:
                    fish_array.append(new_fish)

        print(len(fish_array))

if __name__ == "__main__":
    data_file = ImportData('day_6.data')
    fish_counter = FishCounter(data_file.dataset)
    fish_counter.countFish(80)

    
