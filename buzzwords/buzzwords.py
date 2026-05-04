from collections import defaultdict
from functools import cache

p = 31
mod = 805306457

def getHash(char: chr):
    return ord(char)

@cache
def getPow(power: int):
    return (p ** power) % mod

while (True):
    inputLine = input().replace(" ", "")
    if inputLine == "": # stop at end of file
        break

    initialHash = 0

    # for each posible size of substring
    for size in range(1,len(inputLine)):
        buzzwords = defaultdict(int)

        # set initial hash
        initialHash = (initialHash * p + getHash(inputLine[size-1])) % mod # initial hash is equal to the last enitial hash, but added a extra character
        totalHash = initialHash 
        
        buzzwords[totalHash] += 1

        # for each possible starting position of the substring
        for i in range(1, len(inputLine) - (size-1)):
            # move the hash one to the right
            totalHash = (totalHash - getHash(inputLine[i-1]) * getPow(size - 1)) % mod # removing value of leftmost char 
            totalHash = (totalHash * p) % mod # multiply by p
            totalHash = (totalHash + getHash(inputLine[i + size -1])) % mod # add the new right most element
            buzzwords[totalHash] += 1

        maxAccurences = max(buzzwords.values())
        if maxAccurences <= 1:
            break

        print(maxAccurences)
    print()