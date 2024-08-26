import networkx as nx
import matplotlib.pyplot as plt

def build_graph_from_file(filename):
    """Constrói o grafo com base em um arquivo .txt."""
    graph = nx.Graph()
    
    with open(filename, 'r') as file:
        num_vertices = int(file.readline().strip())
        
        # Adiciona os vértices ao grafo
        graph.add_nodes_from(str(i) for i in range(num_vertices))
        
        # Lê as arestas do arquivo
        while True:
            line = file.readline().strip()
            if line == "-1":
                break
            u, v = line.split()
            graph.add_edge(u, v)
    
    return graph

def max_independent_set(graph):
    """Encontra um conjunto independente usando uma heurística de grau."""
    independent_set = set()
    
    # Obter uma lista de vértices ordenada por grau
    sorted_vertices = sorted(graph.nodes(), key=lambda v: graph.degree(v))
    
    # Conjunto de vértices removidos
    removed_vertices = set()
    
    for vertex in sorted_vertices:
        # Verificar se o vértice pode ser adicionado ao conjunto independente
        if vertex not in removed_vertices:
            # Adicionar o vértice ao conjunto independente
            independent_set.add(vertex)
            # Remover o vértice e seus vizinhos do grafo
            removed_vertices.add(vertex)
            removed_vertices.update(graph.neighbors(vertex))
    
    return independent_set

def plot_graph(graph, independent_set):
    """Plota o grafo e destaca o conjunto independente."""
    pos = nx.spring_layout(graph)  # Layout do grafo
    
    # Desenha todos os nós e arestas
    nx.draw(graph, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=500, font_size=16)
    
    # Destaca o conjunto independente
    nx.draw_networkx_nodes(graph, pos, nodelist=independent_set, node_color='lightgreen', node_size=500)
    
    plt.title("Grafo com Conjunto Independente Destacado")
    plt.savefig('graph.png')  # Salva o gráfico como um arquivo
    plt.close()  # Fecha a figura para liberar memória

# Exemplo de uso
if __name__ == "__main__":
    # Construir o grafo a partir do arquivo
    graph = build_graph_from_file("testes/in1.txt")
    
    # Encontrar o conjunto independente
    max_set = max_independent_set(graph)
    print("Conjunto Independente:", max_set)
    
    # Plotar o grafo e destacar o conjunto independente
    plot_graph(graph, max_set)
