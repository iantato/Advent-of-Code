from os import getcwd

# Day 8 --- Part One --- Matchsticks
def calc_space(items: list):
    
    # - Initialize value.
    total_len = 0
    
    # - Iterate through the items in the given
    #   digital copy from Santa.
    for item in items:
        # - Get the difference of the total character
        #   from string literals and the in-memory
        #   by using eval() function to turn the string
        #   literal into a encoded string.
        total_len += len(item) - len(eval(item))
    
    return total_len


# Day 8 --- Part Two --- Matchsticks
def encoded_space(items : list):
    
    total_len = 0
    
    # - Encoding the string literals with proper string encoding
    #   makes it so that you're only trying to find the encoded
    #   strings on the equation. Hence, we are only computing for the
    #   added literals.
    for item in items:
        total_len += item.count('"') + item.count('\\') + 2
        
    return total_len



DIR = getcwd() + '\\2015\\input'
file = open(DIR + '\\day8.txt').read().splitlines()

print(calc_space(file))
print(encoded_space(file))