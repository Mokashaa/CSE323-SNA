import sys
import networkx as nx
import matplotlib.pyplot as plt
import copy

G = nx.Graph()
labels = []
nx.set_node_attributes(G, labels, 'labels')
labels.append('a')
labels.append('b')
labels.append('c')
labels.append('d')
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 4.3)]
G.add_weighted_edges_from(elist)
H = nx.Graph()
labels = []
nx.set_node_attributes(H, labels, 'labels')
labels.append('a')
labels.append('b')
labels.append('c')
labels.append('d')
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 4.3)]
H.add_weighted_edges_from(elist)
L = nx.Graph()
labels = []
nx.set_node_attributes(L, labels, 'labels')
labels.append('a')
labels.append('b')
labels.append('c')
labels.append('d')
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 4.3)]
L.add_weighted_edges_from(elist)

a = nx.degree_centrality(G)
b = []
m = min(a.values())
for e in a.values():
    b.append(500 + (e*2*3*5*7)**1.5)
print(b)
print(a)

nx.draw(G, with_labels=True, node_size=b)
plt.savefig("degree.png")  # save as png
plt.close()

a = nx.closeness_centrality(H)
b = []
m = min(a.values())
for e in a.values():
    b.append(500 + (e*2*3*5*7)**1.5)
print(b)
print(a)

nx.draw(H, with_labels=True, node_size=b)
plt.savefig("closeness.png")  # save as png
plt.close()

a = nx.betweenness_centrality(L)
b = []
m = min(a.values()) + 1
for e in a.values():
    b.append(500 + (e*2*3*5*7)**1.5)
print(b)
print(a)

nx.draw(L, with_labels=True, node_size=b)
plt.savefig("betweenness.png")  # save as png
