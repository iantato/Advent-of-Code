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

        self.order = dict(list(zip(list(string.ascii_letters), [num for num in range(1, 53)])))

        self._init_file()

    
    def _init_file(self) -> list:
        with open(self.path + "\\input.txt", 'r') as file:
            self._inp = [comp.strip('\n') for comp in file.readlines()]


    def compare(self) -> int:
        
        sum = 0

        for rucksack in self._inp:

            priority = tuple(set([let for let in rucksack[: len(rucksack) // 2]]).intersection([let for let in rucksack[len(rucksack) // 2:]]))
            sum += self.order[priority[0]]

        return sum

    
    def badge_total(self) -> int:

        sum = 0

        for index in range(3, len(self._inp) + 3, 3):
            
            group_raw = self._inp[index - 3 : index]
            group_processed = list([list(dict.fromkeys(x)) for x in group_raw])
            group_flattened = list([f for l in group_processed for f in l])
            
            badge = dict({key : group_flattened.count(key) for key in group_flattened})
            priority = max(badge, key = badge.get)

            sum += self.order[priority]

        return sum


if __name__ == '__main__':
    rucksack = Rucksack(dir_path)
    print(rucksack.badge_total())