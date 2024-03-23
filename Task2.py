# Завдання 2

# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, 
# який було розроблено у першому завданні.

# Далі порівняйте результати виконання обох алгоритмів для цього графа, 
# висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

import networkx as nx

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
    # DFS
    dfs_tree = nx.dfs_tree(G, source='New York')
    print(f"DFS: \n{list(dfs_tree.edges())}\n")

    # BFS
    bfs_tree = nx.bfs_tree(G, source='New York')
    print(f"BFS: \n{list(bfs_tree.edges())}\n")

    #Пояснення результату у README.md

if __name__ == "__main__":
    main()