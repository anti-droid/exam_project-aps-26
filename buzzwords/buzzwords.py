from collections import defaultdict
def getHash(char: chr):
    return ord(char)

p = 2^31

inputLine = input().replace(" ", "")

while (inputLine != ""):
    for size in range(1,len(inputLine)):
        totalHash = 0
        buzzwords = defaultdict(int)

        # set initial hash
        for i in range(size):
            totalHash *= p 
            totalHash += getHash(inputLine[i])
        
        totalHash = totalHash % 20000000
        buzzwords[totalHash] += 1


        for i in range(1, len(inputLine)):
            j = i + (size-1)
            if j >= len(inputLine):
                break
            totalHash -= getHash(inputLine[i-1]) * p ** (size-1)
            totalHash *= p
            totalHash += getHash(inputLine[j])
            totalHash = totalHash % 20000000
            buzzwords[totalHash] += 1

        maxAccurences = 0
        for value in buzzwords.values():
            maxAccurences = max(maxAccurences, value)
        
        if maxAccurences <= 1:
            break
        print(maxAccurences)

    print()
    inputLine = input().replace(" ", "")