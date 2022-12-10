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
                                    'Lose' : (('A', 'Z'), ('B', 'X'), ('C', 'Y')),
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
    

    def accurate_total(self) -> int:
        
        #@# ~~> Initialize Variables <~~ #@#
        #@# ~~> Initialize Scores
        condition = dict({
                            'X' : 'Lose',
                            'Y' : 'Draw',
                            'Z' : 'Win'
                        })
        equivalent = dict({
                            'A' : 0,
                            'B' : 1,
                            'C' : 2,

                            'X' : 1,
                            'Y' : 2,
                            'Z' : 3
                          })
        score = 0

        #@# ~~> FOR loop to calculate the total score <~~ #@#
        #@# ~~> The 2nd column is the condition that says what we need to do (Wether to win, draw or lose)
        #@# ~~> We then try to find how we can fulfill condition by finding the existing pattern in the hashmap
        for game in self._inp:
            selected_condition = condition[game[1]]
            assumed_result = self.encrypted_strat[selected_condition][equivalent[game[0]]]
            
            if selected_condition == 'Draw':
                score += 3 + equivalent[assumed_result[1]]
            elif selected_condition == 'Win':
                score += 6 + equivalent[assumed_result[1]]
            else:
                score += equivalent[assumed_result[1]]
        
        #@# ~~> Return the total score <~~ #@#
        return score