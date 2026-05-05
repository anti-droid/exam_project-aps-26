from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(graph,u,dest,seen):
    if u in seen:
        return (False,seen)
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > 0:
            if v == dest:
                return (True,[(u,v)])
            suc, p = dfs(graph,v,dest,seen)
            if suc:
                p.append((u,v))
                return (True,p)
    return (False,seen)

def flow(graph, src,dest):
    current_flow = 0
    while True:
        ispath, p = dfs(graph,src,dest, set())
        if not ispath:
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
    for j in range(1,n+1):
        for ts in range(s):
            Graph[(j,ts)][j,ts+1] = g

    m = int(input())
    for j in range(m):
        med = int(input())
        Graph[(med,s)][sink] = g
    
    r = int(input())
    for j in range(r):
        a, b, p, t = map(int,input().split())
        for ts in range(s+1-t):
            Graph[(a,ts)][(b,ts+t)] = p

    flow_value = flow(Graph, source, sink)
    print(flow_value)