# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:47:44 2026

@author: erene
"""

import networkx as nx
import matplotlib.pyplot as plt

# 1. Graf (Ağ) Oluşturma
# Yönlendirilmemiş (undirected) bir graf oluşturuyoruz çünkü yollar gidiş-geliş.
G = nx.Graph()

# 2. Düğümleri (Nodes) Ekleme (Toplam 7 Düğüm)
# Bunlar teknik ekibin durak noktaları, şubeler ve hedeflerdir.
nodes = ["Merkez IT", "Sube A", "Sube B", "Sube C", "Sube D", "Veri Merkezi", "Fabrika"]
G.add_nodes_from(nodes)

# 3. Kenarları (Edges) ve Ağırlıkları Ekleme (Toplam 9 Kenar)
# Ağırlıklar (weight), lokasyonlar arasındaki seyahat süresini (dakika cinsinden) temsil eder.
edges = [
    ("Merkez IT", "Sube A", 15),
    ("Merkez IT", "Sube B", 20),
    ("Sube A", "Sube C", 10),
    ("Sube B", "Sube C", 12),
    ("Sube B", "Sube D", 25),
    ("Sube C", "Veri Merkezi", 30),
    ("Sube C", "Sube D", 18),
    ("Sube D", "Fabrika", 15),
    ("Veri Merkezi", "Fabrika", 20)
]

# Kenarları grafa ağırlıklarıyla birlikte ekliyoruz
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# 4. Optimizasyon Modelinin Çalıştırılması: Shortest Path (Dijkstra Algoritması)
# Problem: Merkez IT'den Fabrika'ya en kısa (en hızlı) sürede nasıl gidilir?
source_node = "Merkez IT"
target_node = "Fabrika"

# En kısa yolu ve toplam süreyi hesaplama
shortest_path = nx.shortest_path(G, source=source_node, target=target_node, weight='weight')
shortest_path_length = nx.shortest_path_length(G, source=source_node, target=target_node, weight='weight')

print(f"Acil Durum Rotası: {source_node} -> {target_node}")
print(f"Bulunan En Kısa Yol: {' -> '.join(shortest_path)}")
print(f"Toplam Tahmini Varis Süresi: {shortest_path_length} dakika")

# 5. Görselleştirme (Network Visualization)
plt.figure(figsize=(10, 6))
# Düğümlerin konumlarını belirleme (bahar yayı modeli)
pos = nx.spring_layout(G, seed=42) 

# Tüm ağı çizdirme
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2500, font_size=10, font_weight='bold', edge_color='gray')

# Kenar ağırlıklarını (dakikaları) çizgilerin üzerine yazdırma
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Bulunan en kısa yolu kırmızı ve kalın renkle vurgulama
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title("IT Saha Servis Yönlendirme Ağı ve En Kısa Yol (Kırmızı)", fontsize=14)
# Görseli kaydetme (Hocanın beklediği dosya yapısı için)
plt.savefig("network_visualization.png")
plt.show()