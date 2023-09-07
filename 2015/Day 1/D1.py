
from os import getcwd

# Day 1 --- Part 1 --- Not Quite Lisp
def get_floor_level(data) -> int:
    
    # Initialize the floor level.
    level : int = 0
    
    for floor in data:
        
        # '(' = Santa go up one floor.
        # ')' = Santa go down one floor.
        match floor:
            case '(':
                level += 1
            case ')':
                level -= 1

    return level

# Day 1 --- Part 2 --- Not Quiet Lisp
def basement(data) -> int:
    
    # Initialize Santa's current position.
    position: int = 0
    # Initialize the floor level.
    level : int = 0
        
    for floor in data:
        
        # '(' = Santa go up one floor.
        # ')' = Santa go down one floor.
        match floor:
            case '(':
                level +=1
            case ')':
                level -=1
        
        # The position of the character is linear.
        position += 1
        
        # Checks if Santa is in the basement.
        if (level == -1):
            break
    
    return position



DIR = getcwd() + '\\input'
file = open(DIR + '\\day1.txt').read()

print(get_floor_level(file))
print(basement(file))