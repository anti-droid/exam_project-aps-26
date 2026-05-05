In order to be able to make a maxflow algorithm for this we need to construct a graph that includes the timestamp for each node at every time stamp.

Since there is no requirement for a person to be ending on a spicific node (if they die anyway) all we need to do is take all "time spicific" edges and cut them up into each timestamp:
meaning edge a, b, p, t, with t = 3 and p = 2 will now be:
(a, ab1, p) -> (ab1, ab2, p) -> (ab2, ab3, p) -> (ab3, b, p)
With all edges connected to b still connected to b

And from the source "copying" each node in the original graph and adding a "waiting step" for each timestamp

This can in the worst case expand the size of the graph with max(t) * max(s) = 100 * 100 = 10000 (rettere * 1/2 også men det er ligemeget)
**This can be optimized by instead of doing each timestamp of a road into a uniqe edge, we can modify bfs with a "time sensitive" priority queue**

(CPU time limit is 6 sec.)
Meaning that the worst case timecomplexity will be O(n+r)*t*s = 2000 * 10000 = 20000000 = 2 * 10^7


The max amount of nodes we will have is: (s+1)*n, since t can never be grater than s

Actual pseudo code:

n = int(input())
i, g, s = map(int,input().split())
m = int(input())
Graph = {}

(we deal with the medical facilities later)
(maybe it should just be from each medical f to the sink with infinite flow)

r = int(input())
for j in range(r):
    a, b, p, t = map(int,input().split)
    for k in range(t):
        (add from a -> ab1 ... ab(t-1) -> abt)
    (add abt -> b)

for j in range(s):
    (replicate the graph for each node)

(use Edmonds–Karp algorithm to find maxflow, because it uses bfs, and then we can terminate it when we reach graph depth of s(maybe s+1 depending on how we do sink with medical facilities)

print(min(max_flow,g))
