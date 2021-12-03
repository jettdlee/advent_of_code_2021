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
            dataset = self.__filter_dataset(dataset, index, oxygen_value)
            if len(dataset) <= 1:
                break

        self.oxygen = self.__convertBinaryToDecimal(dataset[0])
        print('Calculated Oxygen: ', self.oxygen)

    def calculateCoDos(self):
        dataset = self.dataset.copy()
        for index in range(len(self.dataset[0])):
            bits_in_index_position = self.__getBitsOnPosition(dataset, index) 
            values, counts = self.__countBits(bits_in_index_position)
            if counts[0] == counts[1]:
                co_2_value = 0
            else:
                co_2_value = values[np.argmin(counts)]
            dataset = self.__filter_dataset(dataset, index, co_2_value)
            if len(dataset) <= 1:
                break

        self.co_dos = self.__convertBinaryToDecimal(dataset[0])
        print('Calculated CO dos: ', self.co_dos)

    def calculatePowerConsumption(self):
        print("Power Consumption: ", self.gamma * self.epsilon)

    def calculateLifeSupportRating(self):
        print("Life Support Rating: ", self.oxygen * self.co_dos)

    def __getBitsOnPosition(self, dataset, index):
        binary_array = []
        for bits in dataset:
            binary_array.append(int(bits[index]))
        return np.array(binary_array)

    def __convertBinaryToDecimal(self, binary):
        return int(binary, 2)

    def __countBits(self, array):
        return np.unique(array, return_counts=True)

    def __filter_dataset(self, dataset, index, value):
        filtered_dataset = []
        for data in dataset:
            if data[index] == str(value):
                filtered_dataset.append(data)
        return filtered_dataset

if __name__ == "__main__":
    data_file = ImportData("day_3.data", False)
    power = PowerThing(data_file.dataset)
    power.calculateGammaRate()
    power.calculateEpsilonRate()
    power.calculatePowerConsumption()
    power.calculateOxygen()
    power.calculateCoDos()
    power.calculateLifeSupportRating()

    
