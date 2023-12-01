from os import getcwd

def best_route(distances: list):
    
    distances = list([i.split(" = ") for i in distances])
    lowest_distance = 0
    
    for route in distances:
        location = route[0].split(" to ")
        
        for i in distances:
            if i[0].startswith(location[1]):
                print(location[0], location[1], i)
            elif i[0].startswith(location[0]):
                print(location[0], location[1], i)
            
    # lowest_distance = 0
    
    # for i in distances:
        
    #     location, distance = i.split(' = ')
    #     location = location.split(" to ")
        
    #     print(distances.count())
        


DIR = getcwd() + '\\2015\\input'
file = open(DIR + '\\day9.txt').read().splitlines()

best_route(file)