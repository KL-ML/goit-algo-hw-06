import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


graph = nx.Graph()
graph.add_edges_from(
    [
        ('C1', 'H1', {"weight": 1}), 
        ('C1', 'N1', {"weight": 3}), 
        ('N1', 'C1', {"weight": 3}),
        ('N2', 'C1', {"weight": 3}),
        ('N2', 'C2', {"weight": 3}),
        ('C2', 'H2', {"weight": 1}), 
        ('C2', 'H3', {"weight": 1}), 
        ('C2', 'H4', {"weight": 1}),
        ('N2', 'C3', {"weight": 3}),
        ('C3', 'C4', {"weight": 4}), 
        ('C3', 'C5', {"weight": 4}), 
        ('C5', 'C3', {"weight": 4}),
        ('O1', 'C4', {"weight": 2}), 
        ('C4', 'O1', {"weight": 2}),
        ('N1', 'C5', {"weight": 3}),
        ('N3', 'C5', {"weight": 3}), 
        ('N3', 'C6', {"weight": 3}), 
        ('N3', 'C7', {"weight": 3}),
        ('C6', 'H5', {"weight": 1}), 
        ('C6', 'H6', {"weight": 1}), 
        ('C6', 'H7', {"weight": 1}),
        ('C7', 'O2', {"weight": 2}), 
        ('O2', 'C7', {"weight": 2}),
        ('N4', 'C7', {"weight": 3}), 
        ('N4', 'C8', {"weight": 3}), 
        ('N4', 'C4', {"weight": 3}),
        ('C8', 'H8', {"weight": 1}), 
        ('C8', 'H9', {"weight": 1}), 
        ('C8', 'H10', {"weight": 1}),
    ]
)

for start_element in graph.nodes:
    shortest_paths = dijkstra(graph, start_element)
    print(f"Найкоротші шляхи від `{start_element}`: {shortest_paths}<br>")