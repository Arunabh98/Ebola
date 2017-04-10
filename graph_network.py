import networkx as nx 
import matplotlib.pyplot as plt 

g = nx.Graph()
g.add_nodes_from([1,2,3,4,5])

g.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 3), (1, 5), (2, 5)])
color_map = []
for node in g:
    if node <2:
        color_map.append('blue')
    else: color_map.append('green') 
print color_map         


color_map[1] = 'blue'

nx.draw(g, node_color=color_map,with_labels=True)

plt.show()
