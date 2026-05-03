import random

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

lines = 10000
lineLength = 1000

with open("random.txt", "w") as file: 
    for _ in range(lines):
        for _ in range(lineLength):
            file.write(chars[random.randint(0,len(chars) - 1)])

        file.write('\n')
    file.write('\n')
