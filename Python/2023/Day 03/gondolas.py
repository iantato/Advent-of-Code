
'''

--- Advent of Code 2023 ---

Day 3: Gear Ratios
https://adventofcode.com/2023/day/3

You and the Elf eventually reach a gondola lift station; he says the gondola lift will 
take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. 
"Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still 
be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but 
nobody can figure out which one. If you can add up all the part numbers in the engine 
schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of 
the engine. There are lots of numbers and symbols you don't really understand, but apparently 
any number adjacent to a symbol, even diagonally, is a "part number" and should be included 
in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:
  467..114..
  ...*......
  ..35..633.
  ......#...
  617*......
  .....+.58.
  ..592.....
  ......755.
  ...$.*....
  .664.598..
In this schematic, two numbers are not part numbers because they are not adjacent 
to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a 
symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the 
part numbers in the engine schematic?


--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs 
to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, 
the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. 
There stands the engineer, holding a phone in one hand and waving with the other. You're 
going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is 
any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of 
multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that 
the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:
  467..114..
  ...*......
  ..35..633.
  ......#...
  617*......
  .....+.58.
  ..592.....
  ......755.
  ...$.*....
  .664.598..
In this schematic, there are two gears. The first is in the top left; it 
has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in 
the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear 
because it is only adjacent to one part number.) Adding up all of the gear ratios 
produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

'''

import os

class Gondola:
    
    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()
    
    # These functions uses recursion in order to find the full
    # numbers from a single digit.
    # Uses a list for the number buffer so that we're able to use the
    # reverse function when we're checking the left decimals.
    # It returns a string which will be converted into an integer later on.
    def check_decimal_right(self, row: int, index: int, number_buffer: list) -> str:
        if index <= len(self.input[row]) - 1:
            if self.input[row][index].isdigit():
                number_buffer.append(self.input[row][index])
                return self.check_decimal_right(row, index + 1, number_buffer)
            else:
                return ''.join(number_buffer)
        else:
            return ''.join(number_buffer)
    
    def check_decimal_left(self, row: int, index: int, number_buffer: list) -> str:
        if self.input[row][index].isdigit() and index >= 0:
            number_buffer.append(self.input[row][index])
            return self.check_decimal_left(row, index - 1, number_buffer)
        else:
            number_buffer.reverse()
            return ''.join(number_buffer)
    
    # == Part One ==>
    def get_gears(self) -> int:
        
        # Initialize the gear's sum.
        out = 0
        
        # Loop through the multi-dimensional array and use the row's index
        # along with the character's indexes in order to loop through.
        for row, line in enumerate(self.input):
            for index, char in enumerate(line):
                # Check if the current character is a symbol.
                if not char.isdigit() and char != '.':
                    # Initialize variables to check whether a decimal
                    # is above/below a symbol so that we don't have to check
                    # the diagonals because the diagonals may be a part
                    # of the digit.
                    above_isdigit = False
                    below_isdigit = False
                    
                    # Check the digit above the current symbol.
                    if row - 1 >= 0:
                        if self.input[row - 1][index].isdigit():
                            num = (self.check_decimal_left(row - 1, index, list([])) + 
                                   self.check_decimal_right(row - 1, index + 1, list([])))
                            above_isdigit = True
                            out += int(num)
                            
                    # Check the digit below the current symbol.
                    if row + 1 <= len(self.input) - 1:
                        if self.input[row + 1][index].isdigit():
                            num = (self.check_decimal_left(row + 1, index, list([])) +
                                   self.check_decimal_right(row + 1, index + 1, list([])))
                            below_isdigit = True
                            out += int(num)
                    
                    # Check the digit directly to the left of the symbol.
                    if index - 1 >= 0:
                        if self.input[row][index - 1].isdigit():
                            num = self.check_decimal_left(row, index - 1, list([]))
                            out += int(num)
                    
                    # Check the digit directly to the right of the symbol.
                    if index + 1 <= len(self.input[row]) - 1:
                        if self.input[row][index + 1].isdigit():
                            num = self.check_decimal_right(row, index + 1, list([]))
                            out += int(num)
                            
                    # Check the diagonals only when there are no digits above.
                    if not above_isdigit:
                        # Check the digit to the upper left of the symbol.
                        if row - 1 >= 0 and index - 1 >= 0:
                            if self.input[row - 1][index - 1].isdigit():
                                num = self.check_decimal_left(row - 1, index - 1, list([]))
                                out += int(num)

                        # Check the digit to the upper right of the symbol.
                        if row - 1 >= 0 and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row - 1][index + 1].isdigit():
                                num = self.check_decimal_right(row - 1, index + 1, list([]))
                                out += int(num)
                                
                    # Check the diagonals only when there are no digits below.
                    if not below_isdigit:
                        # Check the digit to the lower left of the symbol.
                        if row + 1 <= len(self.input) - 1 and index - 1 >= 0:
                            if self.input[row + 1][index - 1].isdigit():
                                num = self.check_decimal_left(row + 1, index - 1, list([]))
                                out += int(num)
                        
                        # Check the digit to the lower right of the symbol.
                        if row + 1 <= len(self.input) and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row + 1][index + 1].isdigit():
                                num = self.check_decimal_right(row + 1, index + 1, list([]))
                                out += int(num)
                    
        return out
    
    # == Part Two ==>
    def gear_ratio(self) -> int:
        
        out = 0
        
        # Uses same loop as the get_gears function. Instead of adding the sum
        # into the output variable immediately, we first check if there are two
        # numbers that are adjacent to the * symbol and then multiply them to get
        # the output.
        for row, line in enumerate(self.input):
            for index, char in enumerate(line):
                
                # Conditional statement for finding the * symbols.
                if char == '*':
                    gears = list([])
                    above_isdigit = False
                    below_isdigit = False
                    
                    # Check upper row.
                    if row - 1 >= 0:
                        if self.input[row - 1][index].isdigit():
                            num = (self.check_decimal_left(row - 1, index, list([])) + 
                                   self.check_decimal_right(row - 1, index + 1, list([])))
                            above_isdigit = True
                            gears.append(int(num))
                            
                    # Check lower row.
                    if row + 1 <= len(self.input) - 1:
                        if self.input[row + 1][index].isdigit():
                            num = (self.check_decimal_left(row + 1, index, list([])) +
                                   self.check_decimal_right(row + 1, index + 1, list([])))
                            below_isdigit = True
                            gears.append(int(num))
                    
                    # Check left.
                    if index - 1 >= 0:
                        if self.input[row][index - 1].isdigit():
                            num = self.check_decimal_left(row, index - 1, list([]))
                            gears.append(int(num))
                    
                    # Check right.
                    if index + 1 <= len(self.input[row]) - 1:
                        if self.input[row][index + 1].isdigit():
                            num = self.check_decimal_right(row, index + 1, list([]))
                            gears.append(int(num))
                            
                    ## Check diagonals
                    # Check upper.
                    if not above_isdigit:
                        if row - 1 >= 0 and index - 1 >= 0:
                            if self.input[row - 1][index - 1].isdigit():
                                num = self.check_decimal_left(row - 1, index - 1, list([]))
                                gears.append(int(num))

                        if row - 1 >= 0 and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row - 1][index + 1].isdigit():
                                num = self.check_decimal_right(row - 1, index + 1, list([]))
                                gears.append(int(num))
                                
                    # Check lower.
                    if not below_isdigit:
                        if row + 1 <= len(self.input) - 1 and index - 1 >= 0:
                            if self.input[row + 1][index - 1].isdigit():
                                num = self.check_decimal_left(row + 1, index - 1, list([]))
                                gears.append(int(num))
                        
                        if row + 1 <= len(self.input) and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row + 1][index + 1].isdigit():
                                num = self.check_decimal_right(row + 1, index + 1, list([]))
                                gears.append(int(num))

                    if len(gears) == 2:
                        out += gears[0] * gears[1]
    
        return out
                        
                    
    


gears = Gondola(os.getcwd() + '\\Day 03\\input.txt')
print(gears.gear_ratio())