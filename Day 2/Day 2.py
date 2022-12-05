'''

Advent of Code - Day 2
Rock Paper Scissors

'''
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class RPS_GameScore:

    #################################################
    ### INITIALIZATION
    #################################################
    def __init__(self, path : str) -> None:
        self.path = path
        
        #@# ~~> Initialize Game Table <~~ #@#
        self.encrypted_strat = dict({
                                    'Draw' : (('A', 'X'), ('B', 'Y'), ('C', 'Z')),
                                    'Win' : (('A', 'Y'), ('B', 'Z'), ('C', 'X')),
                                    'Lose' : (('B', 'X'), ('C', 'Y'), ('A', 'Z')),
                                    })

        #@# ~~> Initialize input variable <~~ #@#
        self._init_file()


    #################################################
    ### OPEN FILE AND RECORD DATA
    #################################################
    def _init_file(self) -> list:

        with open(self.path + "\\input.txt", 'r') as file:
            #@# ~~> Create a list of tuples where each games are stored <~~ #@#
            self._inp = [tuple(num.replace('\n', '').replace(' ', '')) for num in file.readlines()]


    #################################################
    ### GET TOTAL SCORE
    #################################################
    def total_score(self) -> int:

        #@# ~~> Initialize Variables <~~ #@#
        #@# ~~> Initialize Scores
        equivalent = dict({
                            'X' : 1,
                            'Y' : 2,
                            'Z' : 3
                          })
        score = 0

        #@# ~~> FOR loop to calculate the total score <~~ #@#
        #@# ~~> Draw = 3, Win = 6, Lose = 0
        for game in self._inp:
            if (game in self.encrypted_strat['Draw']):
                score += 3 + equivalent[game[1]]
            elif (game in self.encrypted_strat['Win']):
                score += 6 + equivalent[game[1]]
            else:
                score += equivalent[game[1]]

        #@# ~~> Return the total score <~~ #@#
        return score



if __name__ == '__main__':
    score = RPS_GameScore(dir_path)
    print(score.total_score())