import pdb
import numpy as np

from helpers.import_data import ImportData

class SyntaxSystem:
    def __init__(self, dataset):
        self.dataset = dataset
        self.opening_characters = ['(', '[', '{', '<']
        self.closing_sequence = { ')': '(', ']': '[', '}': '{' ,'>': '<' }
        self.error_score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
        self.closing_scores = { '(': 1, '[': 2, '{': 3, '<': 4 } 

    def getScoreForCorruptedSyntax(self):
        score = 0
        for row in self.dataset:
            rowCorrupt, corruptChar = self.__rowCorrupt(row)
            if rowCorrupt: 
                score += self.error_score[corruptChar]
        print('Corrupted Score: ', score)

    def getScoreForIncompleteRows(self):
        scores = []
        for row in self.dataset:
            score = 0
            rowCorrupt, remaining_characters = self.__rowCorrupt(row)
            if not rowCorrupt: 
                for char in remaining_characters[::-1]:
                    score = (score * 5) + self.closing_scores[char]
                scores.append(score)
        scores.sort()
        print('Array of scores: ', scores)
        middle = int(round(len(scores) / 2))
        print('Middle Score: ', scores[middle])

    def __rowCorrupt(self, row):
        opening_characters = []
        for char in row:
            if char in self.opening_characters:
                opening_characters.append(char)
            else:
                opening_char = self.closing_sequence[char]
                if opening_char == opening_characters[-1]:
                    del opening_characters[-1]
                else:
                    return True, char
        return False, opening_characters


if __name__ == "__main__":
    data_file = ImportData('day_10.data')
    syntax_system = SyntaxSystem(data_file.dataset)
    syntax_system.getScoreForCorruptedSyntax()
    syntax_system.getScoreForIncompleteRows()
