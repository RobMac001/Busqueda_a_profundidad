import networkx as nx
import matplotlib.pyplot as plt

# Lista de nodos
nodos = list(range(50))
# nodos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)

# Lista de aristas
aristas = [
    (0, 29), (0, 46), (0, 21), (0, 14), (0, 38), (0, 31),
    (1, 41), (1, 31), (1, 21), (1, 17), (2, 9), (2, 26),
    (2, 5), (2, 25), (2, 4), (3, 18), (3, 30), (3, 47),
    (4, 28), (4, 9), (4, 8), (5, 44), (5, 12), (6, 37),
    (6, 10), (7, 23), (7, 22), (7, 39), (9, 19), (9, 28),
    (9, 27), (11, 33), (13, 25), (13, 38), (13, 29), (14, 26),
    (14, 28), (14, 39), (15, 22), (15, 31), (15, 19), (15, 41),
    (16, 46), (16, 26), (16, 38), (16, 27), (17, 40), (17, 29),
    (18, 45), (18, 42), (18, 35), (18, 33), (18, 47), (20, 36),
    (20, 49), (20, 42), (22, 26), (22, 34), (23, 31), (23, 32),
    (23, 40), (24, 31), (24, 44), (25, 38), (26, 31), (27, 32),
    (29, 48), (29, 41), (30, 47), (30, 37), (33, 36), (33, 49),
    (34, 48), (35, 45), (36, 45), (37, 49), (37, 45), (37, 47),
    (38, 41), (40, 48), (41, 44), (42, 49), (43, 48), (45, 47)
]

# Crear un objeto de grafo dirigido
G = nx.DiGraph()

# Agregar nodos y aristas al grafo
G.add_nodes_from(nodos)
G.add_edges_from(aristas)

# Dibujar el grafo
pos = nx.spring_layout(G)  # Posiciones para el diseño del grafo
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, edge_color='gray', linewidths=0.5, arrowsize=8)

# Mostrar la visualización
plt.show()
