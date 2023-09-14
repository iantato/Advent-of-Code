
from os import getcwd

# Day 6 --- Part One --- Probably a Fire Hazard
    # Create grid.
def grid(size : int) -> list:
    
    # Grid needs to be a dictionary so that we can determine
    # whether a certain position's light is turned on or off.
    grid = dict({})
    
    # Create a grid with x, y positions
    for y in range(size):
        for x in range(size):
            grid[(x, y)] = 0
        
    return grid
    
    # Solve the lights problem.
def lights(instructions : list, grid : dict) -> int:
    
    # Create a copy of the grid dictionary.
    lights = grid.copy()
    
    for line in instructions:
        
        line = line[:-1].split(' ')
        # 'toggle' or 'turn'.
        action = line[0]
        
        # Check if the keyword is 'toggle' or 'turn'.
        match action:
            
            case 'toggle':
                
                # Create a tuple with integers inside of them for the
                # coordinates.
                ini_coord = tuple(map(int, line[1].split(',')))
                max_coord = tuple(map(int, line[3].split(',')))
                
                ini_x = ini_coord[0]
                ini_y = ini_coord[1]
                max_x = max_coord[0]
                max_y = max_coord[1]
                
                # Loop the grid cells to toggle them on or off.
                for x in range(ini_x, max_x + 1):
                    for y in range(ini_y, max_y + 1):
                        
                        # Check whether the light in a cell is already turned on or off
                        # and then toggle them off or on depending on their value.
                        # 1 = on | 2 = off.
                        mode = lights.get((x, y))

                        if mode == 0:
                            lights[(x, y)] = 1
                        else:
                            lights[(x, y)] = 0
                
            case 'turn':
                
                # 'on' or 'off'
                mode = line[1]
                
                # Create a tuple with integers inside of them for the
                # coordinates.
                ini_coord = tuple(map(int, line[2].split(',')))
                max_coord = tuple(map(int, line[4].split(',')))
                
                ini_x = ini_coord[0]
                ini_y = ini_coord[1]
                max_x = max_coord[0]
                max_y = max_coord[1]
                
                # Check if you have to turn the lights 'off' or 'on'
                match mode:
                    
                    case 'on':
                        
                        # Sets the light of the cell into 'on' state.
                        # 1 = on.
                        for x in range(ini_x, max_x + 1):
                            for y in range(ini_y, max_y + 1):
                                lights[(x, y)] = 1
                    
                    case 'off':
                        
                        # Sets the light of the cell into 'off' state.
                        # 0 = off.
                        for x in range(ini_x, max_x + 1):
                            for y in range(ini_y, max_y + 1):
                                lights[(x, y)] = 0
    
    return sum(lights.values())



DIR = getcwd() + '\\2015\\input'
file = open(DIR + '\\day6.txt').readlines()

print(lights(file, grid(1000)))