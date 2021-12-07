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
            new_fishes = []
            for fish in fish_array:
                new_fish = fish.decrementDay()
                if new_fish is not None:
                    new_fishes.append(new_fish)
            fish_array.extend(new_fishes)

        array = [0] * 8
        for fish in fish_array:
            array[fish.lifespan] += 1
        print(array)
        print('Fish Count:', len(fish_array))

class FishCounterV2:
    def __init__(self, dataset):
        self.dataset = list(map(int, dataset[0].split(',')))
        self.spawn_at_day = 8
        self.reset_to_day = 6
        self.fish_array = [0] * self.spawn_at_day

    def countFish(self, days):
        self.__setupInitialFishes()

        for iterations in range(days):
            new_fish_day = self.fish_array.copy()
            for day in range(len(self.fish_array)):
                if day == self.spawn_at_day - 1:
                    new_fish_day[day] = self.fish_array[0]
                elif day == self.reset_to_day - 1:
                    new_fish_day[day] = self.fish_array[day+1] + self.fish_array[0]
                else:
                    new_fish_day[day] = self.fish_array[day+1]

            self.fish_array = new_fish_day
            print('Fish Count:', new_fish_day)

        print('Fish Count:', np.sum(self.fish_array))

    def __setupInitialFishes(self):
        for lifespan in self.dataset:
            self.fish_array[lifespan] += 1

if __name__ == "__main__":
    data_file = ImportData('day_6.data')
    fish_counter = FishCounter(data_file.dataset)
    print('After 80 days')
    fish_counter.countFish(8)

    fish_counter_2 = FishCounterV2(data_file.dataset)
    print('After 256 days')
    fish_counter_2.countFish(8)


    
