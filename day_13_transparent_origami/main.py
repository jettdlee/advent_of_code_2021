import pdb
import numpy as np
from helpers.import_data import ImportData

class Origami:
    def __init__(self, dataset):
        self.dataset = dataset
        self.paper_length = 11
        self.paper_height = 15
        self.__setupPaper()
        self.__setupMarks()
        self.__setupFoldInstructions()

    def fold(self):
        for fold in self.fold_instructions:
            axis = fold[0]
            position = fold[1]
            if axis == 'x':
                top = self.paper[:position]
                bottom = self.paper[position+1:]
            else:
                left = []
                right = []
                for row in self.paper:
                    left.append(row[:position])
                    right.append(row[position+1:])

    def mergePaper(self, paper1, paper2):

    def __setupPaper(self):
        self.paper = []
        for height in range(self.paper_height):
            self.paper.append(['.'] * self.paper_length)

    def __setupMarks(self):
        for row in self.dataset:
            if row == '':
                break
            else:
                x, y = row.split(',')
                self.paper[int(y)][int(x)] = '#'

    def __setupFoldInstructions(self):
        self.fold_instructions = []
        for row in self.dataset:
            if 'fold along' in row:
                axis, position = row.split('=')
                self.fold_instructions.append([axis[-1], int(position)])
            else:
                continue
    
    def printPaper(self):
        for row in self.paper:
            print(row)
        
if __name__ == "__main__":
    data_file = ImportData('test1.data')
    origami = Origami(data_file.dataset)
    origami.fold()

