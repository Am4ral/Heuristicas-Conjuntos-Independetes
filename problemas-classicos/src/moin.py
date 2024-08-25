import itertools
import matplotlib.pyplot as plt
import networkx as nx

def is_independent(graph, subset):
    """Verifica se o subconjunto dado de vértices é independente."""
    for u, v in itertools.combinations(subset, 2):
        if v in graph[u]:
            return False
    return True

def max_independent_set(graph):
    """Encontra o maior conjunto independente usando força bruta."""
    vertices = list(graph.keys())
    max_set = []
    
    for r in range(1, len(vertices) + 1):
        for subset in itertools.combinations(vertices, r):
            if is_independent(graph, subset):
                if len(subset) > len(max_set):
                    max_set = subset
    
    return max_set

def build_graph_from_file(filename):
    """Constrói o grafo com base em um arquivo .txt."""
    graph = {}
    
    with open(filename, 'r') as file:
        num_vertices = int(file.readline().strip())
        
        # Inicializa os vértices no grafo
        for i in range(num_vertices):
            vertex = str(i)  # Usa números como vértices: 0, 1, 2, etc.
            graph[vertex] = []
        
        # Lê as arestas do arquivo
        while True:
            line = file.readline().strip()
            if line == "-1":
                break
            u, v = line.split()
            graph[u].append(v)
            graph[v].append(u)
    
    return graph

def plot_graph(graph, independent_set):
    """Plota o grafo e destaca o conjunto independente."""
    G = nx.Graph()
    
    # Adiciona nós e arestas ao grafo
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor in neighbors:
            if not G.has_edge(node, neighbor):
                G.add_edge(node, neighbor)
    
    pos = nx.spring_layout(G)  # Layout do grafo
    
    # Desenha todos os nós e arestas
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=500, font_size=16)
    
    # Destaca o maior conjunto independente
    nx.draw_networkx_nodes(G, pos, nodelist=independent_set, node_color='lightgreen', node_size=500)
    
    plt.title("Grafo com Conjunto Independente Destacado")
    plt.show()

# Exemplo de uso
if __name__ == "__main__":
    graph = build_graph_from_file("problemas-classicos/testes/in10.txt")
    
    max_set = max_independent_set(graph)
    print("O maior conjunto independente é:", max_set)
    
    plot_graph(graph, max_set)
