from os import getcwd

# Day 5 --- Part One --- Doesn't He Have Intern-Elves For This? ---
def nice(data) -> int:
    
    # Initialize the number for how many are nice.
    nice = 0
    
    for line in data:
        # Create a list out of the characters from
        # a line.
        line = [char for char in line[:-1]]
        
        # --- Vowels Block ---
        # Vowels tuple.
        vowel = ('a', 'e', 'i', 'o', 'u')
        # Initialize the vowel counter.
        vowels = 0
        
        for char in line:
            
            if char in vowel:
                vowels += 1

        # If vowel is less than 3, skip the current loop.
        if vowels < 3:
            continue
        # ---
        # --- Duplicate Character Block ---
        # Last character storage initialization.
        last_char = ''
        # Check if there are character duplications in a row.
        dupe = False
        
        for char in line:
            
            if char == last_char:
                dupe = True
                break
            last_char = char
        
        # If there are no duplicates in a row, skip the current loop.
        if dupe is False:
            continue
        # ---
        # --- Not In String Block ---
        # Restricted strings tuple.
        restricted_strings = ('ab', 'cd', 'pq', 'xy')
        # Check if there are restricted strings in the line.
        restricted = False
        
        # The for loop uses len so that we can instead use the indexing for
        # the list.
        for index in range(0, len(line) - 1):
            string = line[index] + line[index + 1]
            
            if string in restricted_strings:
                restricted = True
                break
        
        # If there are no restricted strings in the line.
        if restricted is True:
            continue
        # ---
        
        # Add one to the nice if all the conditions were met.
        nice += 1  

    return nice

# Day 5 --- Part Two --- Doesn't He Have Intern-Elves For This? ---
def very_nice(data) -> int:
    
    nice = 0
    
    for line in data:
        # Create a list out of the characters from
        # a line.
        line = [char for char in line[:-1]]
        print(line)
        



DIR = getcwd() + '\\2015\\input'
file = open(DIR + '\\day5.txt').readlines()

print(nice(file))
