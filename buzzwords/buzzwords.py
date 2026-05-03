from collections import defaultdict
import time
from functools import cache
import math

def getHash(char: chr):
    return ord(char)

startTime = time.time() 

p = 31

@cache
def getPow(power: int):
    return (p ** power) % 805306457

inputLine = input().replace(" ", "")

# for each line in the input
while (inputLine != ""):
    output = [] 
    initialHash = 0

    # for each posible size of the substring
    for size in range(1,len(inputLine)):
        totalHash = 0
        buzzwords = defaultdict(int)

        # set initial hash
        initialHash = (initialHash * p + getHash(inputLine[size-1])) % 805306457 # initial hash is equal to the last enitial hash, but added a extra character
        totalHash = initialHash 
        
        buzzwords[totalHash] += 1

        counter = 0
        # for each posibble starting position of the substring
        for i in range(1, len(inputLine) - (size-1)):
            counter += 1
            # move the hash one to the right by first removing the value of the left most value, times it all by p, add the right most ellemtnt and modulo it by a constant
            totalHash = ((totalHash - getHash(inputLine[i-1]) * getPow(size - 1)) * p + getHash(inputLine[ i + size -1])) % 805306457 
            buzzwords[totalHash] += 1

        maxAccurences = 0
        for value in buzzwords.values():
            maxAccurences = max(maxAccurences, value)

        if maxAccurences <= 1:
            break

        output.append(f"{maxAccurences}\n")
    
    print("".join(output))
    inputLine = input().replace(" ", "")

print("Time:", time.time() - startTime)
