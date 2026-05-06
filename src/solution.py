import networkx as nx
import matplotlib.pyplot as plt

# 1. Graph Creation
G = nx.Graph()

# 2. Adding Nodes (Total 7 Nodes)
nodes = [
    "Headquarters", "Branch Office A", "Branch Office B", 
    "Branch Office C", "Branch Office D", "Data Center", "Production Facility"
]
G.add_nodes_from(nodes)

# 3. Adding Edges and Weights (Total 9 Edges)
edges = [
    ("Headquarters", "Branch Office A", 15),
    ("Headquarters", "Branch Office B", 20),
    ("Branch Office A", "Branch Office C", 10),
    ("Branch Office B", "Branch Office C", 12),
    ("Branch Office B", "Branch Office D", 25),
    ("Branch Office C", "Data Center", 30),
    ("Branch Office C", "Branch Office D", 18),
    ("Branch Office D", "Production Facility", 15),
    ("Data Center", "Production Facility", 20)
]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# 4. Running the Optimization Model
source_node = "Headquarters"
target_node = "Production Facility"

shortest_path = nx.shortest_path(G, source=source_node, target=target_node, weight='weight')
shortest_path_length = nx.shortest_path_length(G, source=source_node, target=target_node, weight='weight')

print(f"Emergency Route: {source_node} -> {target_node}")
print(f"Optimal Path Found: {' -> '.join(shortest_path)}")
print(f"Total Estimated Travel Time: {shortest_path_length} minutes")

# 5. Network Visualization
plt.figure(figsize=(12, 7))

pos = nx.spring_layout(G, seed=42) 

nx.draw(G, pos, with_labels=True, node_color='#A0CBE2', node_size=3000, 
        font_size=9, font_weight='bold', edge_color='gray')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

# IT kelimesi çıkarılmış, güncel ve temiz başlık
plt.title("Field Service Network: Shortest Path Analysis", fontsize=14, fontweight='bold')

plt.savefig("../results/network_visualization.png")
plt.show()