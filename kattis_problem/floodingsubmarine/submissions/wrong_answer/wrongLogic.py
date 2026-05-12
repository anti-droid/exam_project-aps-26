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
viseted = set()
holesDirection = [0 for _ in range(n)]
def setHoleDirection(ver: int): 
    viseted.add(ver)

    if ver in holes:
        holesDirection[ver] = 1
        return 1
    
    sum = 0
    for child in G[ver]:
        if child not in viseted:
            sum += setHoleDirection(child)
    holesDirection[ver] = sum
    return sum
setHoleDirection(0)


visited = [False] * n

print(G)

src = 0
q = deque()
visited[src] = True
q.append(src)

while q:
    if len(q) >= p:
        print(q)
        break

    curr = q.popleft()

    if curr in holes:
        q.append(curr)
        continue

    # visit all the unvisited
    # neighbours of current node
    for x in G[curr]:
        if not visited[x]:
            visited[x] = True
            next = x 
            while len(G[next]) == 2: # if the next node only has one child (not including the node we are on currently)
                for child in G[next]:
                    next = child

            q.append(next)


print(holesDirection)
    