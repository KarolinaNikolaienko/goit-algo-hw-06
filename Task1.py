# Завдання 1

# Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі 
# (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).
# Візуалізуйте створений граф, проведіть аналіз основних характеристик 
# (наприклад, кількість вершин та ребер, ступінь вершин).

import networkx as nx
import matplotlib.pyplot as plt

def main():
    graph = {
        "New York" : ["London", "Rio de Janeiro", "Aleksandria", "Cape Town"],
        "London" : ["New York", "Rio de Janeiro"],
        "Aleksandria" : ["Dubai", "London", "New York", "Rio de Janeiro"],
        "Sydney" : ["Cape Town", "Mumbai", "Singapore", "Tokio"],
        "Dubai": ["Mumbai", "Singapore", "Aleksandria", "Sydney", "Cape Town"],
        "Tokio" : ["Singapore", "Long Beach"],
        "Cape Town" : ["New York", "Rio de Janeiro", "London", "Sydney"],
        "Rio de Janeiro" : ["New York", "Cape Town", "London"],
        "Mumbai" : ["Dubai", "Sydney", "Singapore"],
        "Singapore" : ["Tokio", "Cape Town", "Mumbai", "Dubai"],
        "Long Beach" : ["Tokio"]
    }

    G = nx.Graph(graph)
    G.remove_node("Long Beach")
    pos = {}
    coord = [(10, 100), (30, 105), (50, 90), (110, 10), (60, 80), (110, 100), (40, 15), 
             (20, 18), (80, 70), (100, 50), (110, 110)]
    for i, node in enumerate(G.nodes()):
        pos[node] = coord[i]
    nx.draw(G, pos, with_labels=True, arrows=True)

    print(f"Amount of nodes: {G.number_of_nodes()}\n")
    print(f"Amount of nodes: {G.number_of_edges()}\n")
    print(f"Degree centrality: \n{nx.degree_centrality(G)}\n")
    print(f"Closeness centraliry: \n{nx.closeness_centrality(G)}\n")
    print(f"Betweenness centraliry: \n{nx.betweenness_centrality(G)}\n")
    print(f"Average shortest path length {nx.average_shortest_path_length(G)}\n")
    print(f"Shortest path between New York and Sydney: {nx.shortest_path(G, "New York", "Sydney")}")

    plt.show()

if __name__ == "__main__":
    main()