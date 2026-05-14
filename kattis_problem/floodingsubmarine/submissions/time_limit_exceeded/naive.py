from itertools import combinations
from collections import defaultdict
n,e,h,p = map(int,input().split())

G = defaultdict(lambda: set())
H = set()
E = []

for _ in range(e):
    v,u = map(int,input().split())
    E.append((v,u))
    G[v].add(u)
    G[u].add(v)

for _ in range(h):
    H.add(int(input()))

def dfs_for_holes(this, seen, G, pluged):
    if this in H:
        return True
    seen.add(this)
    for v in G[this]:
        if v in seen or v in pluged[this]:
            continue
        if dfs_for_holes(v,seen,G,pluged):
            return True
    return False

max_saved = 0
for e in combinations(E,p):
    Pluged = defaultdict(lambda: set())
    for v,u in e:
        Pluged[v].add(u)
        Pluged[u].add(v)
    s = set()
    foundHole = dfs_for_holes(0,s,G,Pluged)
    if not foundHole:
        max_saved = max(max_saved,len(s))
    
print(max_saved)