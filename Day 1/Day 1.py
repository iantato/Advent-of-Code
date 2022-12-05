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
        max_cal = 0
        sum = 0

        #@# ~~> FOR loop to to find which elf is carrying the largest calorie <~~ #@#
        #@# ~~> it keeps summing up the calories until the '' separator is reached
        for calorie in self._inp:
            if (calorie == ''):
                
                if (sum > max_cal):
                    max_cal = sum

                sum = 0

            else:
                sum += int(calorie)

        #@# ~~> Return the biggest calorie <~~ #@#
        return max_cal
                    


if __name__ == '__main__':
    calorie = CalorieCount(dir_path)
    print(calorie.count())