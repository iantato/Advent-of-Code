'''

Advent of Code - Day 2
Rock Paper Scissors

'''
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class RPS_GameScore:

    def __init__(self, path : str) -> None:
        self.path = path
        
        self.encrypted_strat = dict({
                                    'Rock' : ('A', 'X'),
                                    'Paper' : ('B', 'Y'),
                                    'Scissors' : ('C', 'Z')
                                    })

    
    def total_score(self) -> int:
        
        with open(self.path + "\\input.txt") as inp:
            pass

        return 0