from collections import defaultdict
from collections import deque

#input reading
n, e, h, p = map(int,input().split())

G = defaultdict(lambda: set())
for i in range(e): # load graph
    v1, v2 = map(int, input().split())
    G[v1].add(v2)
    G[v2].add(v1)
holes = set()
for i in range(h):
    holes.add(int(input()))

# creating holeDirection
visited = set()
holesDirection = [0 for _ in range(n)]
def setHoleDirection(ver: int): 
    global visited
    visited.add(ver)

    if ver in holes:
        holesDirection[ver] = 1
        return 1
    
    sum = 0
    for child in sorted(G[ver]):
        if child not in visited:
            sum += setHoleDirection(child)
    holesDirection[ver] = sum
    return sum
setHoleDirection(0)


visited = set()
q = deque()
visited.add(0)
q.append(0)

while q:
    all_is_holes = True
    for node in list(q):
        if node not in holes:
            all_is_holes = False
            break

    if (len(q) >= p or all_is_holes) and not q[0] == 0:
        break

    curr = q.popleft()

    if curr in holes:
        q.append(curr)
        continue

    for x in sorted(G[curr]):
        if x not in  visited:
            visited.add(x)
            next = x 
            
            while (len(G[next]) == 2 or (holesDirection[next] == 1 and len(G[next]) > 1)) and next not in holes: # if the next node only has one child (not including the node we are on currently)
                if len(G[next]) == 2:
                    for child in sorted(G[next]):
                        if child not in visited:
                            visited.add(child)
                            next = child
                    continue

                for child in sorted(G[next]):
                    if holesDirection[child] == 1 and child not in visited:
                        visited.add(child)
                        next = child
                        break 

            q.append(next)
plugLocations = set(q)

areaCount = 0
def calArea(node: int, pre: int):
    global areaCount
    if node in plugLocations:
        return
    
    areaCount += 1

    for child in G[node]:
        if child != pre:
            calArea(child, node)
calArea(0, -1)
print(areaCount)