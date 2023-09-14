
from os import getcwd

# Day 6 --- Part One --- Probably a Fire Hazard
    # Solve the lights problem.
def lights(instructions : list) -> int:
    
    # Generate a 1000x1000 grid by using multi-dimensional arrays.
    grid = [[0]*1000 for _ in range(1000)]
    # Initialize the opened lights counter.
    lights = 0
    
    for line in instructions:
        
        # Split the line into four different phrases from the right.
        # 'turn/toggle on/off', 'initial coords', through, 'maximum coords'.
        # The 3 is used to indicate the 1st and 2nd index to be combined and stop 
        # at the 3rd.
        action, ini_coords, _, max_coords = line.strip().rsplit(' ', 3)
        # Turn the string coordinates into a tupled integer.
        x_ini, y_ini = tuple(map(int, ini_coords.rsplit(',')))
        x_max, y_max = tuple(map(int, max_coords.rsplit(',')))

        for x in range(x_ini, x_max + 1):
            for y in range(y_ini, y_max + 1):
                
                match action:
                    
                    # 1 = On.
                    case 'turn on':
                        grid[x][y] = 1
                    
                    # 0 = Off.
                    case 'turn off':
                        grid[x][y] = 0
                    
                    case 'toggle':
                        
                        if grid[x][y] == 0:
                            grid[x][y] = 1
                        else:
                            grid[x][y] = 0
    
    for rows in grid:
        lights += sum(rows)
        
    return lights

# Day 6 --- Part Two --- Probably a Fire Hazard
def brightness(instructions: list) -> int:
    
    grid = [[0]*1000 for _ in range(1000)]
    brightness = 0
    
    for line in instructions:
        
        # Split the line into four different phrases from the right.
        # 'turn/toggle on/off', 'initial coords', through, 'maximum coords'.
        # The 3 is used to indicate the 1st and 2nd index to be combined and stop 
        # at the 3rd.
        action, ini_coords, _, max_coords = line.strip().rsplit(' ', 3)
        # Turn the string coordinates into a tupled integer.
        x_ini, y_ini = tuple(map(int, ini_coords.rsplit(',')))
        x_max, y_max = tuple(map(int, max_coords.rsplit(',')))
        
        for x in range(x_ini, x_max + 1):
            for y in range(y_ini, y_max + 1):
                
                match action:
                    
                    # On = +1.
                    case 'turn on':
                        grid[x][y] += 1
                    
                    # Off = -1 | Minimum of zero.
                    case 'turn off':
                        if grid[x][y] > 0:
                            grid[x][y] -= 1
                    
                    case 'toggle':
                        
                        grid[x][y] += 2
    
    for rows in grid:
        brightness += sum(rows)
        
    return brightness



DIR = getcwd() + '\\2015\\input'
file = open(DIR + '\\day6.txt').readlines()

print(lights(file))
print(brightness(file))