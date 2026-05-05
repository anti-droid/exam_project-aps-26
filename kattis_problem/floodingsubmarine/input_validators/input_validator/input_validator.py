import sys
import re

n = 0
e = 0 
h = 0 
p = 0

line = sys.stdin.readline()
if line.endswith('\n'):
    line = line[0:len(line)-1]
else: 
    sys.exit(43)
    print("no newline where it was expected in first line")
reg1 = r"[1-9][0-9]* [1-9][0-9]* [1-9][0-9]* [1-9][0-9]*"
if not re.fullmatch(reg1, line):
    print("First line is not 4 valid numbers")
    sys.exit(43)

try: 
    n, e, h, p = map(int,line.split())
except:
    print("could not parce first line")
    sys.exit(43)

mentionedNodes = set()

# edges
for _ in range(e):
    edge = sys.stdin.readline()
    if edge.endswith('\n'):
        edge = edge[0:len(edge)-1]
    else: 
        print("no newline where it was expected in edges")
        sys.exit(43)

    if not re.fullmatch(r"[0-9][0-9]* [0-9][0-9]*", edge):
        print("edge is not valid")
        sys.exit(43)
    
    try:
        n1, n2 = map(int,edge.split())

        if n1 < 0 or n1 >= n or n2 < 0 or n2 >= n:
            print("node mentioned is not within the range [0..N-1]")
            sys.exit(43)

        mentionedNodes.add(n1)
        mentionedNodes.add(n2)
            
    except:
        print("could not parce edge")
        sys.exit(43)


if len(mentionedNodes) != n:
    print("mentiond nodes in edges does not match N")
    sys.exit(43)

#holes
mentionedHoles = set()
for _ in range(h):
    holeLine = sys.stdin.readline()
    if holeLine.endswith('\n'):
        holeLine = holeLine[0:len(holeLine)-1]
    else: 
        print("no newline where it was expected in holes")
        sys.exit(43)
    if not re.fullmatch(r"[0-9][0-9]*",holeLine):
        print("hole is not valid")
        sys.exit(43)

    
    try:
        hole = int(holeLine)

        if hole < 0 or hole >= n :
            print("hole is not within the range [0..N-1]")
            sys.exit(43)

        mentionedHoles.add(hole)
            
    except:
        print("could not parce hole")
        sys.exit(43)

if len(mentionedHoles) != h:
    print("incorrect number of holes")
    sys.exit(43)

endingLine = sys.stdin.readline()
if endingLine != "":
    print("Random ending junk '" + endingLine + "'")
    sys.exit(43)

sys.exit(42)


