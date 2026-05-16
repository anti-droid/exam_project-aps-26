from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**4)

n, e, h, p = map(int,input().split())

#a dict keeping the verticies that the node has edges to in 'e' 
# and keeping the values for the solution with each plug combination in 'p'
G = defaultdict(lambda: {'e':set(),'p':[]})
for i in range(e): # load graph
    v1, v2 = map(int, input().split())
    G[v1]['e'].add(v2)
    G[v2]['e'].add(v1)

holes = set()
for i in range(h):
    holes.add(int(input()))


#finds the optimal solution for each amount of plugs from two other solutions
def compare_lists(l1,l2,maxplugs):
    result = []
    for plug in range(maxplugs):
        if plug != 0:
            result.append(result[plug-1])
        else:
            result.append(-n)
        for i in range(plug+1):
            if len(l2) <= i:
                break
            result[plug] = max(l2[i]+l1[plug-i],result[plug])
    return result

# traverse the graph and find the optimal solution from a given vertex 
# by reccersivly finding the best solution for each of its children
def traverse(v, fromv):
    if v in holes:
        G[v]['p'].append(-n)
        G[v]['p'].append(0)
        return 1
    maxplugs = 1
    for u in G[v]['e']:
        if u == fromv:
            continue
        maxplugs += traverse(u,v)
    maxplugs = min(maxplugs,p)
    guess = [1 for i in range(maxplugs+1)]
    for u in G[v]['e']:
        if u == fromv:
            continue
        guess = compare_lists(guess, G[u]['p'], maxplugs+1)
    guess[1] = max(guess[1],0)
    G[v]['p'] = guess
    return maxplugs
        
traverse(0,-1)

if p > h: #if this is the case, the answer will always be the same as for p=h which is calculated
    print(G[0]['p'][-1])
else:
    print(G[0]['p'][p])