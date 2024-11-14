import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


# Define infinity as a large number to indicate no connection
INF = float('inf')

# Adjacency matrix for the graph based on the provided image
graph = np.array([
    [0,   2,   7,   INF, INF, INF, INF],
    [2,   0,   INF, 1,   5,   INF, INF],
    [7,   INF, 0,   3,   INF, 10,  INF],
    [INF, 1,   3,   0,   6,   4,   INF],
    [INF, 5,   INF, 6,   0,   INF, 3],
    [INF, INF, 10,  4,   INF, 0,   3],
    [INF, INF, INF, INF, 3,   3,   0]
])

print("We will be using Prims Algorithm to find the MST ")


#first we define the node labels

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'Z']
node_indices = {i: nodes[i] for i in range(len(nodes))}


#Next is the prims algorithm implimentation

def prims_mst(matrix):
    num_nodes = len(matrix)
    selected_nodes = [False] * num_nodes
    selected_nodes[0] = True # start from node A or in other words index 0

    mst_edge = []

    print("Step by step Construction of MST: ")

    for _ in range(num_nodes):
        min_weight = INF
        u, v = -1, -1
        for i in range(num_nodes):
                if selected_nodes[i]:
                    for j in range(num_nodes):
                         if not selected_nodes[j] and 0 <  matrix[i][j] < min_weight:
                              min_weight = matrix[i][j]
                              u, v = i, j
        if u != -1 and v != -1:
             mst_edge.append((u, v, min_weight))
             selected_nodes[v] = True
             print(f"Added edge: {node_indices[u]} - {node_indices[v]} with weight {min_weight}")
             visualise_step(matrix, mst_edge)

    return mst_edge

#below is the function to visualise the mst step by step

def visualise_step(matrix, mst_edges):
    G = nx.Graph()
    for i in range(len(matrix)):
        G.add_node(nodes[i])
    for u, v, weight in mst_edges:
         G.add_edge(nodes[u], nodes[v], weight=weight)
    
    pos = nx.spring_layout(G, seed=42)  # Layout for visualization
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(nodes[u], nodes[v]): weight for u, v, weight in mst_edges})
    plt.title("MST Step-by-Step")
    plt.show()



mst_edges = prims_mst(graph)

def visualize_final_mst(matrix, mst_edges):
    G = nx.Graph()
    for i in range(len(matrix)):
        G.add_node(nodes[i])
    for u, v, weight in mst_edges:
        G.add_edge(nodes[u], nodes[v], weight=weight)

    pos = nx.spring_layout(G, seed=42)  # Layout for visualization
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(nodes[u], nodes[v]): weight for u, v, weight in mst_edges})
    plt.title("Final MST")
    plt.show()

# Display the final MST
print("Final MST:")
visualize_final_mst(graph, mst_edges)

