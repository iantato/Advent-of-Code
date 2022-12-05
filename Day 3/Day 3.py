'''

Advent of Code - Day 3
Rucksack Reorganization

'''
import os
import string

dir_path = os.path.dirname(os.path.realpath(__file__))

class Rucksack:

    def __init__(self, path : str) -> None:
        self.path = path

        self._init_file()

    
    def _init_file(self) -> list:
        with open(self.path + "\\input.txt", 'r') as file:
            self._inp = [comp.strip('\n') for comp in file.readlines()]


    def compare(self) -> int:
        
        order = dict(list(zip(list(string.ascii_letters), [num for num in range(1, 53)])))
        sum = 0

        for rucksack in self._inp:

            priority = tuple(set([let for let in rucksack[: len(rucksack) // 2]]).intersection([let for let in rucksack[len(rucksack) // 2:]]))
            sum += order[priority[0]]

        return sum


if __name__ == '__main__':
    rucksack = Rucksack(dir_path)
    rucksack.compare()