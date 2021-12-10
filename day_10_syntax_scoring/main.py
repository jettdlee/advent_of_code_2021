import pdb
import numpy as np
import re
from helpers.import_data import ImportData

class SyntaxSystem:
    def __init__(self, dataset):
        self.dataset = dataset
        self.opening_characters = ['(', '[', '{', '<']
        self.closing_sequence = { ')': '(', ']': '[', '}': '{' ,'>': '<' }
        self.error_score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

    def getScoreForCorruptedSyntax(self):
        score = 0
        for row in self.dataset:
            opening_characters = []
            for char in row:
                if char in self.opening_characters:
                    opening_characters.append(char)
                else:
                    opening_char = self.closing_sequence[char]
                    if opening_char == opening_characters[-1]:
                        del opening_characters[-1]
                    else:
                        print(opening_char, ' != ', opening_characters[-1])
                        break
        print('Corrupted Score: ', score)

if __name__ == "__main__":
    data_file = ImportData('day_10.data')
    syntax_system = SyntaxSystem(data_file.dataset)
    syntax_system.getScoreForCorruptedSyntax()
