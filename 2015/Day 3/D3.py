from os import getcwd

# Day 3 --- Part One --- Perfectly Spherical Houses in a Vacuum
def visited(data) -> int:
    
    # Initialize the position of Santa.
    x = 0
    y = 0
    
    # Initialize the list for where Santa has been.
    delivered = [(x, y)]
    
    for direction in data:
        
        match direction:
            # North
            case '^':
                y += 1
            # South
            case 'v':
                y -= 1
            # East
            case '>':
                x += 1
            # West
            case '<':
                x -= 1
                
        delivered.append((x, y))
    
    # Turns the list into a set which deletes all the
    # duplicate values in the list.
    return len(set(delivered))

# Day 3 --- Part Two --- Perfectly Spherical Houses in a Vacuum
def with_robot_visited(data) -> int:
    
    # Initialize Santa's position.
    santa_x = 0
    santa_y = 0
    # Initialize the variable where Santa's directions
    # are going to be stored.
    santa_direction = ''
    # Initialize the list where Santa has been will be stored.
    santa_delivered = [(santa_x, santa_y)]
    
    # Initialize Robo-Santa's position.
    robo_x = 0
    robo_y = 0
    # Initialize the variable where Robo-Santa's directions
    # are going to be stored.
    robo_direction = ''
    # Initialize the list where Robo-Santa has been will be stored.
    robo_delivered = [(robo_x, robo_y)]
    
    # Get the directions for Santa by starting at the first character of
    # the input and then skipping the characters by 2.
    for direction in range(0, len(data), 2):
        santa_direction += data[direction]
    
    # Get the directions for Robo-Santa by starting at the second character
    # of the input and then skipping the characters by 2.
    for direction in range(1, len(data), 2):
        robo_direction += data[direction]
    
    # Santa
    for direction in santa_direction:
        
        match direction:
            # North
            case '^':
                santa_x += 1
            # South
            case 'v':
                santa_x -= 1
            # East
            case '>':
                santa_y += 1
            # West
            case '<':
                santa_y -= 1
        
        santa_delivered.append((santa_x, santa_y))
                
    # Robo-Santa
    for direction in robo_direction:
        
        match direction:
            # North
            case '^':
                robo_x += 1
            # South
            case 'v':
                robo_x -= 1
            # East
            case '>':
                robo_y += 1
            # West
            case '<':
                robo_y -= 1
                
        robo_delivered.append((robo_x, robo_y))

    # Combine all the deliveries Robo-Santa and Santa has made.
    delivered = robo_delivered + santa_delivered
    
    return len(set(delivered))
    
        
        
DIR = getcwd() + '\\input'
file = open(DIR + '\\day3.txt').read()

print(visited(file))
print(with_robot_visited(file))
            