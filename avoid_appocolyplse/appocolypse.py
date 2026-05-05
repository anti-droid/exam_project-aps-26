from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def dfs(graph,u,dest,mincap,seen): # returns path to dest
    if u in seen:
        return (False,seen)
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > mincap: # only consider edges with capacity > mincap
            if v == dest:
                return (True,[(u,v)])
            #print(f'explore {u} {v}, {cap}')
            suc, p = dfs(graph,v,dest,mincap,seen)
            if suc:
                p.append((u,v))
                return (True,p)
    return (False,seen)


def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity,c)

    current_flow = 0
    mincap = maxcapacity # set to 0 to disable capacity scaling
    while True:
        #ispath, p_or_seen = bfs(graph,src,dest,mincap)
        ispath, p_or_seen = dfs(graph,src,dest,mincap, set())
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2
                continue
            else:
                return (current_flow,
                        { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in orggraph.items() },
                        p_or_seen)
        p = p_or_seen
        #print("path:", *reversed(p))
        saturation = min( graph[u][v] for u,v in p )
        #print(current_flow,saturation)#,[f"{u[0]}-{u[1]}:{orggraph[u[0]][u[1]]}:{graph[u][v]}" for u,v in p if u[2]==0])
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation

inf = 100
for testcase in range(int(input())):
    n = int(input())
    i, g, s = map(int,input().split())
    sink = (n+1,s+1)
    source = (0,-1)
    Graph = defaultdict(lambda: defaultdict(lambda: int)) 
    
    Graph[source][(i,0)] = g
    for j in range(1,n+1):
        for ts in range(s):
            Graph[(j,ts)][j,ts+1] = inf

    m = int(input())
    for j in range(m):
        med = int(input())
        Graph[(med,s)][sink] = inf
    
    r = int(input())
    for j in range(r):
        a, b, p, t = map(int,input().split())
        for ts in range(s+1-t):
            Graph[(a,ts)][(b,ts+t)] = p

    flow_value, residual_graph, _ = flow(Graph, source, sink)
    print(flow_value)