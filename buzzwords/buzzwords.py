from collections import defaultdict
import time
from functools import cache

def getHash(char: chr):
    return ord(char)

startTime = time.time() 

p = 2^31

@cache
def getPow(power: int):
    return p ** power

inputLine = input().replace(" ", "")


while (inputLine != ""):
    output = [] 
    initialHash = 0

    for size in range(1,len(inputLine)):
        totalHash = 0
        buzzwords = defaultdict(int)

        # set initial hash
        initialHash = initialHash * p + getHash(inputLine[size-1])
        totalHash = initialHash
        
        totalHash = totalHash % 20000000
        buzzwords[totalHash] += 1

        for i in range(1, len(inputLine)):
            j = i + (size-1)
            if j >= len(inputLine):
                break
            totalHash -= getHash(inputLine[i-1]) * getPow(size - 1)
            totalHash *= p
            totalHash += getHash(inputLine[j])
            totalHash = totalHash % 20000000
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
