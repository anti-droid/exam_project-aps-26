from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(graph,u,dest,mincap, seen):
    if u in seen:
        return (False,seen)
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > mincap:
            if v == dest:
                return (True,[(u,v)])
            suc, p = dfs(graph,v,dest,mincap,seen)
            if suc:
                p.append((u,v))
                return (True,p)
    return (False,seen)

def flow(graph, src,dest, maxcapacity):
    current_flow = 0
    mincap = maxcapacity
    while True:
        ispath, p = dfs(graph,src,dest, mincap, set())
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2
                continue
            return (current_flow)
        saturation = min( graph[u][v] for u,v in p )
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation


for testcase in range(int(input())):
    n = int(input())
    i, g, s = map(int,input().split())
    sink = (n+1,s+1)
    source = (0,-1)
    Graph = defaultdict(lambda: defaultdict(int)) 
    
    Graph[source][(i,0)] = g
    for l in range(1,n+1):
        for ts in range(s):
            Graph[(l,ts)][l,ts+1] = g

    m = int(input())
    for _ in range(m):
        med = int(input())
        Graph[(med,s)][sink] = g
    
    r = int(input())
    for _ in range(r):
        a, b, p, t = map(int,input().split())
        for ts in range(s+1-t):
            Graph[(a,ts)][(b,ts+t)] = p

    flow_value = flow(Graph, source, sink, g)
    print(flow_value)