from collections import deque

# Рекурсивна реалізація алгоритму DFS
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Рекурсивна реалізація алгоритму BFS
def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

# Представлення графа за допомогою списку суміжності
graph = {
    'N1': ['C1', 'C5'],
    'N2': ['C1', 'C2', 'C3'],
    'N3': ['C5', 'C6', 'C7'], 
    'N4': ['C7', 'C8', 'C4'],
    'C1': ['H1', 'N1', 'N2'], 
    'C2': ['N2', 'H2', 'H3', 'H4'], 
    'C3': ['C4', 'C5', 'N2'], 
    'C4': ['C3', 'O1', 'N4'], 
    'C5': ['C3', 'N1', 'N3'], 
    'C6': ['N3', 'H5', 'H6', 'H7'], 
    'C7': ['N3', 'O2', 'N4'], 
    'C8': ['N4', 'H8', 'H9', 'H10'],
    'O1': ['C4'], 
    'O2': ['C7'],
    'H1': ['C1'], 
    'H2': ['C2'],
    'H3': ['C2'], 
    'H4': ['C2'], 
    'H5': ['C6'], 
    'H6': ['C6'], 
    'H7': ['C6'],
    'H8': ['C8'], 
    'H9': ['C8'], 
    'H10': ['C8'],
}


# Виклик функції DFS для найбільш середнього елемента, отриманого в першому завдання
print('Depth-first search (DFS):')
dfs_recursive(graph, 'C3')
print()
# Запуск рекурсивного алгоритму BFS
print('Breadth-first search (BFS):')
bfs_recursive(graph, deque(["C3"]))

