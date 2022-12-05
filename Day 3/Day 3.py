'''

Advent of Code - Day 3
Rucksack Reorganization

'''
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Rucksack:

    def __init__(self, path : str) -> None:
        x = 'rNZNWvMZZmDDmwqNdZrWTqhJMhhgzggBhzBJBchQzzJJ'
        print(x[ : len(x) // 2])
        print(x[len(x) // 2 : ])


if __name__ == '__main__':
    rucksack = Rucksack(dir_path)