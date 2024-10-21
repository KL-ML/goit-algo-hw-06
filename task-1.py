import networkx as nx
import matplotlib.pyplot as plt

# Створюємо направлений граф для відображення молекули кофеїну
graph = nx.DiGraph()

# Створюємо вершини по кількості атомів 
graph.add_nodes_from(
    [
        'N1', 'N2', 'N3', 'N4',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
        'O1', 'O2',
        'H1', 'H2','H3', 'H4', 'H5', 'H6', 'H7','H8', 'H9', 'H10', 
    ]
)
# Перелічуємо звʼязки відповідно до формули
graph.add_edges_from(
    [
        ('C1', 'H1'), ('C1', 'N1'), ('N1', 'C1'),
        ('N2', 'C1'),
        ('N2', 'C2'),
        ('C2', 'H2'), ('C2', 'H3'), ('C2', 'H4'),
        ('N2', 'C3'),
        ('C3', 'C4'), ('C3', 'C5'), ('C5', 'C3'),
        ('O1', 'C4'), ('C4', 'O1'),
        ('N1', 'C5'),
        ('N3', 'C5'), ('N3', 'C6'), ('N3', 'C7'),
        ('C6', 'H5'), ('C6', 'H6'), ('C6', 'H7'),
        ('C7', 'O2'), ('O2', 'C7'),
        ('N4', 'C7'), ('N4', 'C8'), ('N4', 'C4'),
        ('C8', 'H8'), ('C8', 'H9'), ('C8', 'H10'),
    ]
)

# перетворюємо граф на ненаправлений для кращої візуалізації
graf_for_visualisation = nx.Graph(graph)
pos = nx.forceatlas2_layout(graf_for_visualisation)

nx.draw_networkx_nodes(
    graf_for_visualisation, pos, node_size=350, 
    nodelist=['N1', 'N2', 'N3', 'N4'], 
    node_color="tab:blue", 
    label="Натрій"
)
nx.draw_networkx_nodes(
    graf_for_visualisation, pos, node_size=450, 
    nodelist=['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'], 
    node_color="#3d3d3d", 
    label="Вуглець"
)
nx.draw_networkx_nodes(
    graf_for_visualisation, pos, node_size=350, 
    nodelist=['O1', 'O2'], 
    node_color="tab:red",
    label="Кисень",
)
nx.draw_networkx_nodes(
    graf_for_visualisation, pos, node_size=200, 
    nodelist=['H1', 'H2','H3', 'H4', 'H5', 'H6', 'H7','H8', 'H9', 'H10'], 
    label="Водень",
    node_color="#f0e5e4", 
    
)
nx.draw_networkx_edges(
    graf_for_visualisation, 
    pos,  
    alpha=0.3, 
    width=2,
    arrows=False
    )

plt.title("Молекула кофеїну")
ax = plt.gca()
ax.margins(0.11)
plt.tight_layout()
plt.axis("off")
plt.legend(['Натрій', 'Вуглець', 'Кисень', 'Водень'])
plt.show()


# Виводимо кількість вершин та ребер
num_nodes = graph.number_of_nodes()
num_edges = graph.number_of_edges()

print(f"\nКількість атомів: {num_nodes}")
print(f"Кількість звʼязків: {num_edges}")


# Знайдемо валентність елементів за допомогою підрахунку ступені кожної вершини
degree_dict = dict(graph.degree())
val_elements = {}
for node, degree in degree_dict.items():
    element = node[0]
    val_elements[element] = str(degree)
print(f"\nВалентність елементів:\nНатрій: {val_elements['N']}, Вуглець: {val_elements['C']}, Кисень: {val_elements['O']}, Водень: {val_elements['H']}")

# Отримаємо найбільш середній елемент за методом посередництва вузла
betweenness_centrality = nx.betweenness_centrality(graph)
sorted_graf = sorted(betweenness_centrality.items(), key=lambda x:x[1])
print(f"\nНайбільш середній елемент за методом посередництва вузла: \n{sorted_graf[-1]}") 
