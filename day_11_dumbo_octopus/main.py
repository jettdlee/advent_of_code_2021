import pdb
import numpy
from helpers.import_data import ImportData

class Octopus:
    def __init__(self, energy):
        self.energy = int(energy)

    def increment(self):
        self.energy += 1

    def flash(self):
        if self.energy > 9:
            return True
        else:
            return False

    def reset(self):
        if self.energy > 9:
            self.energy = 0;

class Grid:
    def __init__(self, dataset):
        self.dataset = dataset
        self.octopus_grid = self.__setupOctopus()

    def countFlashesForSteps(self, steps):
        flash_count = 0
        self.current_state = self.octopus_grid.copy()
        for step in range(steps):
            self.__incrementAllOctopus()
            flash_positions = self.__checkAllFlashes()
            flash_count += len(flash_positions)
            self.__resetOctopusEnergy()

        print(flash_count)

    def firstSynchronousFlash(self):
        self.current_state = self.__setupOctopus()
        step = 0
        print(self.__printState(self.current_state))
        while True:
            step += 1
            self.__incrementAllOctopus()
            flash_positions = self.__checkAllFlashes()
            self.__resetOctopusEnergy()
            if self.__checkSynchronisation():
                break
                
        print(self.__printState(self.current_state))
        print(step)

    def __checkSynchronisation(self):
        sum = 0
        for row in self.current_state:
            for octopus in row:
                sum += octopus.energy
        return sum == 0

    def __incrementAllOctopus(self):
        for row in self.current_state:
            for octopus in row:
                octopus.increment()

    def __checkAllFlashes(self):
        no_more_flashes = False
        flash_positions = []
        while no_more_flashes == False:
            no_more_flashes = True
            for i, row in enumerate(self.current_state):
                for j, octopus in enumerate(row):
                    if octopus.flash() and [i, j] not in flash_positions:
                        no_more_flashes = False
                        flash_positions.append([i, j])
                        self.__incrementSurroundingOctopus(i, j)

        return flash_positions

    def __resetOctopusEnergy(self):
        for row in self.current_state:
            for octopus in row:
                octopus.reset()

    def __incrementSurroundingOctopus(self, x, y):
        positions = [[x-1, y-1], [x-1,y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1,y], [x+1, y+1]]
        max_octo = len(self.current_state[0]) - 1
        for i, j in positions:
            if i < 0 or i > max_octo or j < 0 or j > max_octo:
                continue
            octopus = self.current_state[i][j]
            octopus.increment()

    def __setupOctopus(self):
        array = []
        for row in self.dataset:
            row_array = []
            for energy in row:
                row_array.append(Octopus(energy))
            array.append(row_array)
        return array

    def __printState(self, state):
        for row in state:
            row_energy = []
            for octopus in row:
                row_energy.append(octopus.energy)
            print(row_energy)
        print('-----------------------')

if __name__ == "__main__":
    data_file = ImportData('day_11.data')
    # data_file = ImportData('test.data')
    grid = Grid(data_file.dataset)
    grid.countFlashesForSteps(100)
    grid.firstSynchronousFlash()
