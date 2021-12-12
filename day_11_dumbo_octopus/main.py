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
            self.energy -= 10;

class Grid:
    def __init__(self, dataset):
        self.dataset = dataset
        self.octopus_grid = self.__setupOctopus()

    def countFlashesForSteps(self, steps):
        flash_count = 0
        octopus_state = self.octopus_grid.copy()
        for step in range(steps):
            octopus_state = self.__incrementAllOctopus(octopus_state)
            octopus_state, flash_positions = self.__checkAllFlashes(octopus_state)
            flash_count += len(flash_positions)
            octopus_state = self.__resetOctopusEnergy(octopus_state)
        print(flash_count)

    def __incrementAllOctopus(self, octopus_state):
        state = octopus_state.copy()
        for row in state:
            for octopus in row:
                octopus.increment()
        return state

    def __checkAllFlashes(self, octopus_state):
        state = octopus_state.copy()
        no_more_flashes = False
        flash_positions = []
        while no_more_flashes == False:
            no_more_flashes = True
            for i, row in enumerate(state):
                for j, octopus in enumerate(row):
                    if octopus.flash() and [i, j] not in flash_positions:
                        no_more_flashes = False
                        flash_positions.append([i, j])
                        state = self.__incrementSurroundingOctopus(i, j, state)

        return state, flash_positions

    def __resetOctopusEnergy(self, octopus_state):
        state = octopus_state.copy()
        for row in state:
            for octopus in row:
                octopus.reset()
        return state

    def __incrementSurroundingOctopus(self, x, y, octopus_state):
        state = octopus_state.copy()
        positions = [[x-1, y-1], [x-1,y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1,y], [x+1, y+1]]
        for i, j in positions:
            try:
                octopus = state[i, j]
                octopus.increment()
            except:
                continue
        return state

    def __setupOctopus(self):
        array = []
        for row in self.dataset:
            row_array = []
            for energy in row:
                row_array.append(Octopus(energy))
            array.append(row_array)
        return array

if __name__ == "__main__":
    data_file = ImportData('day_11.data')
    grid = Grid(data_file.dataset)
    grid.countFlashesForSteps(100)
