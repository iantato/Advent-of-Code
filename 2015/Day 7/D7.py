
from os import getcwd

# DAY 7 --- Part One --- Some Assembly Required
def find_signal(commands: list, find_wire: str):
    
    # - Initialize variables
    index = 0
    # - Store cache in the initial memory
    memory = dict({})
    
    # - Keep looping until the signal is found.
    while True:
        
        # - Check if the signal is found.
        try:
            return memory[find_wire]
        except KeyError:
            pass
        
        if index == len(commands):
            index = 0
            
        # - Split the input and output.
        # - We split the signal so that we can manipulate
        #   the numbers' data types, as well as check the
        #   gate.
        signal, wire = commands[index].split(' -> ')
        signal = signal.split(' ')
        
        # - Uses len to determine how many inputs are
        #   accepted in the gates.
        match len(signal):
            
            ##- LOGIC GATES THAT ACCEPTS TWO INPUTS.
            case 3:
                # - Check the first number if integer.
                try:
                    signal[0] = int(signal[0])
                except ValueError:
                    # - Check if the number is in the memory.
                    try:
                        signal[0] = int(memory[signal[0]])
                    except KeyError:
                        index += 1
                        continue
                
                # - Check the second number if integer.
                try:
                    signal[2] = int(signal[2])
                except ValueError:
                    # - Check if the number is in the memory.
                    try:
                        signal[2] = int(memory[signal[2]])
                    except KeyError:
                        index += 1
                        continue
                    
            ##- LOGIC GATES THAT ACCEPTS ONLY ONE INPUT.
            case 2:
                # - Check the number if integer.
                try:
                    signal[1] = int(signal[1])
                except ValueError:
                    # - Check if the number is in the memory.
                    try:
                        signal[1] = int(memory[signal[1]])
                    except KeyError:
                        index += 1
                        continue
            
            ##- NO LOGIC GATES USED
            case _:
                try:
                    signal[0] = int(signal[0])
                    out = signal[0]
                except ValueError:
                    try:
                        signal[0] = int(memory[signal[0]])
                        out = signal[0]
                    except KeyError:
                        index += 1
                        continue
        
        # - Emulate the equation of logic gates.
        if 'AND' in signal:
            out = signal[0] & signal[2]
        elif 'OR' in signal:
            out = signal[0] | signal[2]
        elif 'LSHIFT' in signal:
            out = signal[0] << signal[2]
        elif 'RSHIFT' in signal:
            out = signal[0] >> signal[2]
        elif 'NOT' in signal:
            out = ~ signal[1]

        # - Store the wire and the signal in memory if
        #   it does not exist in memory.
        if wire not in memory:
            memory[wire] = out
        index += 1
        
# DAY 7 --- Part Two --- Some Assembly Required
def override_wire(commands: list, override_signal: str, override_value: int, find_wire: str):
    
    # - Loop through the commands to find the signal that
    #   needs to be overriden.
    for index in range(0, len(commands)):
        signal, wire = commands[index].split(' -> ')
        
        # - Overrides the value of the selected wire.
        if wire == override_signal:
            commands[index] = str(override_value) + ' -> ' + wire
    
    # - Just find the wire with new signal.
    return find_signal(commands, find_wire)
            

DIR = getcwd() + '\\2015\\input'
file = open(DIR + '\\day7.txt').read().splitlines()