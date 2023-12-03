
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

'''

import os
import re

class Gondola:
    
    def __init__(self, input: str) -> None:
        self.input = open(input).read()
        
    def parts(self) -> int:
        
        LINE_LEN = self.input.find('\n') + 1
        self.input = ('.' * LINE_LEN) + self.input + ('.' * LINE_LEN)

        start_index = 0
        num = ""
        
        out = 0
        
        for index in range(0, len(self.input)):
            if self.input[index].isdigit():
                if start_index == 0:
                    start_index = index
                    
                num += self.input[index]
            elif num != '':
                for i in range(start_index, index):
                    if ((not self.input[i + LINE_LEN].isalnum() and self.input[i + LINE_LEN]  != '.')
                        or (not self.input[i + 1].isalnum() and self.input[i + 1] != '.')
                        or (not self.input[i - 1].isalnum() and self.input[i - 1] != '.')
                        or (not self.input[i - LINE_LEN + 1].isalnum() and self.input[i - LINE_LEN + 1] != '.')
                        or (not self.input[i - LINE_LEN - 1].isalnum() and self.input[i - LINE_LEN - 1] != '.')
                        or (not self.input[i + LINE_LEN + 1].isalnum() and self.input[i + LINE_LEN + 1] != '.')
                        or (not self.input[i + LINE_LEN - 1].isalnum() and self.input[i + LINE_LEN - 1] != '.')):
                            out += int(num)
                            start_index = 0
                            num = ""
                            break
                
                start_index = 0
                num = ""
        
        return out
        
        
        
gears = Gondola(os.getcwd() + '\\Day 03\\input.txt')
print(gears.parts())