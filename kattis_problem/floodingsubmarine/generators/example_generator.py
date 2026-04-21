#!/usr/bin/env python3
import networkx as nx
import random
import sys
import matplotlib.pyplot as plt

rand_seed = int(sys.argv[1]) #using 42 as standard its also used elsewhere
random.seed(rand_seed)

n = 4
e = 15
h = 3
p = 2

#G = nx.complete_graph(n) #creates a fully connected graph (could be good for a worst case testcase)
#G = nx.gnm_random_graph(n,e) # creates random connected graph
G = nx.random_lobster(n, 0.5, 0.5, rand_seed)

random_nodes = random.sample(list(G.nodes()), h)

# Print number of nodes (n), edges (e), holes (h), and gates/plugs (p)
# followed by e lines defining the edges, and then h lines defining the holes
print(G.number_of_nodes(), G.number_of_edges(), h, p)
#print edges
for e in G.edges:
    v1, v2 = e
    print(v1,v2)
print(*random_nodes, sep='\n')


#Visual representation of the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
