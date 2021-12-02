import pdb
import numpy as np
from helpers.import_data import ImportData

class DepthChecker:
    def __init__(self, dataset):
        self.dataset = np.array(dataset)
        self.count = 0
        self.countSum = 0

    def findIncreaseMeasurement(self):
        for index in range(len(self.dataset)):
            if index == 0:
                continue 
            if self.dataset[index] > self.dataset[index-1]:
                self.count += 1

    def calcualateSumOfNextDepth(self):
        for index in range(len(self.dataset)):
            if index == 0:
                continue 
            currentSum = self.__getSumOnIndex(index)
            previousSum = self.__getSumOnIndex(index-1)
            if currentSum > previousSum:
                self.countSum += 1

    def __getSumOnIndex(self, index):
        return self.dataset[index:index+3].sum()

if __name__ == "__main__":
    data_file = ImportData("day_1.data", True)
    checker = DepthChecker(data_file.dataset)
    checker.findIncreaseMeasurement()
    print(checker.count)

    checker.calcualateSumOfNextDepth()
    print(checker.countSum)
    
