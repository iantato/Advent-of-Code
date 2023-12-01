
import hashlib

# Day 4 --- Part One --- The Ideal Stocking Stuffer
def mine_5(data) -> int:
    
    # Initialize the first number to be added to the data.
    num = 1
    
    while True:
        # Add the number to data.
        to_hash = data + str(num)
        # Encode the data+num to MD5 hashing and turn it into hexdecimal.
        # Set the string to the first 5 characters.
        hexadecimal = hashlib.md5(to_hash.encode()).hexdigest()[:5]
        
        # Check if the hexadecimal begins in '00000'
        if hexadecimal == '00000':
            break

        num += 1
    
    return num

# Day 4 --- Part Two --- The Ideal Stocking Stuffer
def mine_6(data) -> int:
    
    # Initialize the first number to be added to the data.
    # The number starts at 254,575 because the 5 zeroes can be
    # found in this number.
    num = 254575
    
    while True:
        # Encode the data+num to MD5 hashing and turn it into hexdecimal.
        # Set the string to the first 6 characters.
        to_hash = data + str(num)
        hexadecimal = hashlib.md5(to_hash.encode()).hexdigest()[:6]
        
        # Check if the hexadecimal begins in '000000'
        if hexadecimal == '000000':
            break

        num += 1
    
    return num



file = 'bgvyzdsv'
print(mine_5(file))
print(mine_6(file))