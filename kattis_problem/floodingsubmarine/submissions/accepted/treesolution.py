from collections import defaultdict

n, e, h, p = map(int,input().split())

G = defaultdict(lambda: {'e':set(),'p':[]})
for i in range(e):
    v1, v2 = map(int, input().split())
    G[v1]['e'].add(v2)
    G[v2]['e'].add(v1)

holes = set()
for i in range(h):
    holes.add(int(input()))

#print(G) 
#print(holes)

def compare_lists(l1,l2,maxplugs):
    result = []
    for plug in range(maxplugs):
        result.append(-n)
        for i in range(plug+1):
            if len(l2) <= i:
                break
            result[plug] = max(l2[i]+l1[plug-i],result[plug])
    return result

def traverse(v, fromv):
    if v in holes:
        #print('hole:', v)
        G[v]['p'].append(-n) #0 fucker dig op
        G[v]['p'].append(0)
        return 1
    maxplugs = 1
    for u in G[v]['e']:
        if u == fromv:
            continue
        maxplugs += traverse(u,v)
    maxplugs = min(maxplugs,p)+1
    guess = [1 for i in range(maxplugs)]
    for u in G[v]['e']:
        if u == fromv:
            continue
        #print(v, G[u]['p'], u)
        guess = compare_lists(guess, G[u]['p'], maxplugs)
        #print(v, guess)
    guess[1] = max(guess[1],0)
    G[v]['p'] = guess
    return maxplugs
        

traverse(0,-1)
print(G[0]['p'][p])