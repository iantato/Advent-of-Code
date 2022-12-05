'''

Advent of Code - Day 1
Calorie Counting

'''
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class CalorieCount:

    #################################################
    ### INITIALIZATION
    #################################################
    def __init__(self, path : str) -> None:
        self.path = path

        #@# ~~> Initialize input variable <~~ #@#
        self._init_file()
    

    #################################################
    ### OPEN FILE AND RECORD DATA
    #################################################
    def _init_file(self) -> list:

        with open(self.path + "\\input.txt", 'r') as file:
            #@# ~~> Create the list of calories with no '\n' in the end of the numbers <~~ #@#
            self._inp = [num.strip('\n') for num in file.readlines()]
    

    #################################################
    ### GET LARGEST CALORIE
    #################################################
    def count(self) -> int:
        
        #@# ~~> Initialize Variables <~~ #@#
        s = 0
        max_cal = 0

        #@# ~~> FOR loop to to find which elf is carrying the largest calorie <~~ #@#
        #@# ~~> it keeps summing up the calories until the '' separator is reached
        for calorie in self._inp:
            if (calorie == ''):
                
                if (s > max_cal):
                    max_cal = s

                s = 0

            else:
                s += int(calorie)

        #@# ~~> Return the biggest calorie <~~ #@#
        return max_cal

    
    #################################################
    ### GET TOTAL OF TOP ELVES
    #################################################
    def top_total(self, places : int) -> list:
        
        #@# ~~> Initialize Variables <~~ #@#
        s = 0
        calories = list([])

        #@# ~~> FOR loop to make a list of total calories <~~ #@#
        for calorie in self._inp:
            if (calorie == ''):
                
                calories.append(s)
                s = 0

            else:
                s += int(calorie)

        #@# ~~> Arrange list <~~ #@#
        calories.sort()
        calories.reverse()

        #@# ~~> Return the sum of calories of the top places specified <~~ #@#
        return sum(calories[:places])