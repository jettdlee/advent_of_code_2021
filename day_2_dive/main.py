import pdb
import numpy as np
from helpers.import_data import ImportData

class Submarine:
    def __init__(self, dataset):
        self.dataset = np.array(dataset)
        self.resetPosition()
    
    def moveFromInstructions(self, include_aim=False):
        for instruction in self.dataset:
            direction, spaces = self.__readInstruction(instruction)
            if direction == 'forward':
                self.horizontal_position += spaces
                if include_aim == True:
                    self.depth += self.aim * spaces
            elif direction == 'down':
                if include_aim == True:
                    self.aim += spaces 
                else:
                    self.depth += spaces
            elif direction == 'up':
                if include_aim == True:
                    self.aim -= spaces 
                else:
                    self.depth -= spaces

    def resetPosition(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0

    def __readInstruction(self, instruction):
        instruction_array = instruction.split()
        return instruction_array[0], int(instruction_array[1])

if __name__ == "__main__":
    data_file = ImportData("day_2.data")

    submarine = Submarine(data_file.dataset)
    submarine.moveFromInstructions()
    print("Part1: horizontal: ", submarine.horizontal_position, "depth: ", submarine.depth, "multiply: ", submarine.horizontal_position * submarine.depth)

    submarine.resetPosition()
    submarine.moveFromInstructions(True)
    print("Part1: horizontal: ", submarine.horizontal_position, "depth: ", submarine.depth, "multiply: ", submarine.horizontal_position * submarine.depth)

