import pdb
import numpy as np
from helpers.import_data import ImportData

class PowerThing:

    def __init__(self, dataset):
        self.dataset = np.array(dataset)
        self.gamma = 0
        self.epsilon = 0
        self.oxygen = 0
        self.co_dos = 0

    def calculateGammaRate(self):
        gamma_bits = []
        for index in range(len(self.dataset[0])):
            bits_in_index_position = self.__getBitsOnPosition(self.dataset, index) 
            values, counts = self.__countBits(bits_in_index_position)
            max_value_index = np.argmax(counts)
            gamma_bits.append(values[max_value_index])
        self.gamma = self.__convertBinaryToDecimal(''.join(np.char.mod('%i', gamma_bits)))
        print('Calculated Gamma: ', self.gamma)

    def calculateEpsilonRate(self):
        epsilon_bits = []
        for index in range(len(self.dataset[0])):
            bits_in_index_position = self.__getBitsOnPosition(self.dataset, index) 
            values, counts = self.__countBits(bits_in_index_position)
            min_value_index = np.argmin(counts)
            epsilon_bits.append(values[min_value_index])
        self.epsilon = self.__convertBinaryToDecimal(''.join(np.char.mod('%i', epsilon_bits)))
        print('Calculated Epsilon: ', self.epsilon)

    def calculateOxygen(self):
        dataset = self.dataset.copy()
        for index in range(len(self.dataset[0])):
            bits_in_index_position = self.__getBitsOnPosition(dataset, index) 
            values, counts = self.__countBits(bits_in_index_position)
            if counts[0] == counts[1]:
                oxygen_value = 1
            else:
                oxygen_value = values[np.argmax(counts)]
            dataset = self.__remove_from_dataset(dataset, index, oxygen_value)
        print(dataset)

    def calculatePowerConsumption(self):
        print("Power Consumption: ", self.gamma * self.epsilon)

    def __getBitsOnPosition(self, dataset, index):
        binary_array = []
        for bits in self.dataset:
            binary_array.append(int(bits[index]))
        return np.array(binary_array)

    def __convertBinaryToDecimal(self, binary):
        return int(binary, 2)

    def __countBits(self, array):
        return np.unique(array, return_counts=True)

    def __remove_from_dataset(self, dataset, index, value):
        return np.delete(dataset, np.where(dataset != value))

if __name__ == "__main__":
    data_file = ImportData("day_3.data", False)
    power = PowerThing(data_file.dataset)
    power.calculateGammaRate()
    power.calculateEpsilonRate()
    power.calculatePowerConsumption()
    power.calculateOxygen()
    
