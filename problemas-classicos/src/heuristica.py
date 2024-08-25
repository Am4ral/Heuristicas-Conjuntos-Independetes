import networkx as nx

def independent_set_algorithm(graph):
    # Criar um conjunto independente
    independent_set = set()
    
    # Obter uma lista de vértices ordenada por grau
    sorted_vertices = sorted(graph.nodes(), key=lambda v: graph.degree(v), reverse=True)
    
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

# Exemplo de uso
if __name__ == "__main__":
    # Criar um grafo exemplo
    G = nx.Graph()
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 4)]
    G.add_edges_from(edges)
    
    # Encontrar o conjunto independente
    result = independent_set_algorithm(G)
    print("Conjunto Independente:", result)
