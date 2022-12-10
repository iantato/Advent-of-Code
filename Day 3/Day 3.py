'''

Advent of Code - Day 3
Rucksack Reorganization

'''
import os
import string

dir_path = os.path.dirname(os.path.realpath(__file__))

class Rucksack:

    #################################################
    ### INITIALIZATION
    #################################################
    def __init__(self, path : str) -> None:
        self.path = path

        #@# ~~> Initialize Priority based on Ascii Letter's number in the Alphabet <~~ #@#
        self.order = dict(list(zip(list(string.ascii_letters), [num for num in range(1, 53)])))

        #@# ~~> Initialize input variable <~~ #@#
        self._init_file()


    #################################################
    ### OPEN FILE AND RECORD DATA
    #################################################
    def _init_file(self) -> list:
        with open(self.path + "\\input.txt", 'r') as file:
            self._inp = [comp.strip('\n') for comp in file.readlines()]


    #################################################
    ### COMPARE TWO RUCKSACK AND FIND ERROR
    #################################################
    def compare(self) -> int:
        
        #@# ~~> Initialize Variables <~~ #@#
        sum = 0

        #@# ~~> FOR loop to calculate the sum <~~ #@#
        for rucksack in self._inp:
            
            #@# ~~> Using set to find the duplicates <~~ #@#
            #@# ~~> It transforms the strings into a list of letters first
            priority = tuple(set([let for let in rucksack[: len(rucksack) // 2]]).intersection([let for let in rucksack[len(rucksack) // 2:]]))
            
            #@# ~~> Using the priority, it gets the value of the letter from the dictionary of alphabets <~~ #@#
            sum += self.order[priority[0]]

        #@# ~~> Return the total sum of priority <~~ #@#
        return sum

    
    #################################################
    ### FIND BADGE FROM THREE COMPARTMENTS
    #################################################
    def badge_total(self) -> int:

        sum = 0

        #@# ~~> FOR loop to get each of the three compartments' in the input list <~~ #@#
        for index in range(3, len(self._inp) + 3, 3):
            
            #@# ~~> Get the three elements from the input array <~~ #@#
            group_raw = self._inp[index - 3 : index]
            #@# ~~> Turn string into a list of letters <~~ #@#
            group_processed = list([list(dict.fromkeys(x)) for x in group_raw])
            #@# ~~> Flatten the array of array <~~ #@#
            group_flattened = list([f for l in group_processed for f in l])
            
            #@# ~~> Turn array into a dictionary <~~ #@#
            badge = dict({key : group_flattened.count(key) for key in group_flattened})
            #@# ~~> Get the key of the max value in the dictionary <~~ #@#
            priority = max(badge, key = badge.get)

            #@# ~~> Using the priority, it gets the value of the letter from the dictionary of alphabets <~~ #@#
            sum += self.order[priority]

        #@# ~~> Return the total sum of priority <~~ #@#
        return sum