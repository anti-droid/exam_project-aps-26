from collections import defaultdict
n, e, h, p = map(int,input().split())
print(n,e,500,500)
G = defaultdict(lambda: 0)
for i in range(e): # load graph
    v1, v2 = map(int, input().split())
    print(v1,v2)
    G[v1]+=1
    G[v2]+=1

i=0
for key in G:
    if G[key]==1:
        print(key)
        i+=1
    if i==500:
        break
