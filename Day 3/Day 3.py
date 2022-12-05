'''

Advent of Code - Day 3
Rucksack Reorganization

'''
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Rucksack:

    def __init__(self, path : str) -> None:
        self.path = path
        
        self.init_file()

    
    def init_file(self) -> list:
        with open(self.path + "\\input.txt", 'r') as file:
            self.inp = file.readlines()


    def compare(self) -> None:
        print(self.inp)





if __name__ == '__main__':
    rucksack = Rucksack(dir_path)
    rucksack.compare()