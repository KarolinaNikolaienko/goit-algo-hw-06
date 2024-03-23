# Завдання 3

# Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: 
# додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.

import networkx as nx
import math

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())
    visited = []

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        
        visited.append(current_vertex)
        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

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
    
    # Додаємо вагу для ребер - відстань між точками
    for edge in G.edges():
        G[edge[0]][edge[1]]["weight"] = math.dist(pos[edge[0]],pos[edge[1]])
    
    for node in G.nodes():
        dist = dijkstra(G, node)
        print(f"\nFor node {node}:\n{dist}")


if __name__ == "__main__":
    main()