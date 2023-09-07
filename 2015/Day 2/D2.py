
from os import getcwd

# Day 2 --- Part One --- I Was Told There Would Be No Math
def total_wrapper_paper_sqft(data) -> int:

    # Initialize the total square feet of wrapping paper.
    total_sqf = 0
    
    for dimensions in data:
        # Split the measurement by x as the dimensions is
        # divided by an 'x'.
        # Uses list comprehensions in order to convert the numbers
        # from string to integer data-type.
        measurement = [int(num) for num in dimensions.split('x')]
        
        # Initialize the measurement's variables
        length = measurement[0]
        width = measurement[1]
        height = measurement[2]
        
        # Solve the areas for each combination and store them to a tuple
        # so that we can solve the total_sqf and the slack faster.
        surface = (
                (length*width), 
                (width*height), 
                (height*length)
                )
        
        # Multiply the sum of the area to 2 as we need to get the surface area of
        # the box which can be translated to (2*l*w) + (2*w*h) + (2*h*l).
        # The min(surface) function is used to get the lowest area of the box which
        # is the slack requirement.
        total_sqf += (2*sum(surface)) + min(surface)
    
    return total_sqf

# Day 2 --- Part Two --- I Was Told There Would Be No Math
def ribbon(data) -> int:

    # Initialize the ribbon's total measurement
    ribbon = 0
    
    for dimensions in data:
        # Split the measurement by x as the dimensions is
        # divided by an 'x'.
        # Uses list comprehensions in order to convert the numbers
        # from string to integer data-type.
        measurements = [int(num) for num in dimensions.split('x')]
        # Sort the measurements list to find the shortest side easier
        measurements.sort()
        
        # Compute the shortest distance around its sides
        distance = (measurements[0] + measurements[0] + 
                    measurements[1] + measurements[1])
        # Compute for the cubic feet
        cubic_feet = measurements[0] * measurements[1] * measurements[2]

        ribbon += distance + cubic_feet

    return ribbon



DIR = getcwd() + '\\input'
file = open(DIR + '\\day2.txt').readlines()

print(total_wrapper_paper_sqft(file))
print(ribbon(file))