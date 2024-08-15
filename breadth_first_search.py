from collections import deque

def bfs(graph, start):
    """
    Realiza a pesquisa em largura em um grafo a partir de um nó inicial.

    Parâmetros:
    graph (dict): O grafo representado como um dicionário de listas adjacentes.
    start (str/int): O nó inicial para a BFS.

    Retorna:
    list: Lista de nós visitados na ordem de visitação.
    """
    visited = []  # Lista para manter os nós visitados
    queue = deque([start])  # Fila para os nós a serem explorados
    
    print(f"Iniciando a BFS a partir do nó '{start}'")
    
    while queue:
        # Remove o nó da frente da fila
        node = queue.popleft()
        
        if node not in visited:
            # Marca o nó como visitado
            visited.append(node)
            print(f"Visitando nó: {node}")
            
            # Adiciona os vizinhos não visitados à fila
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    print(f"Adicionando nó vizinho '{neighbor}' à fila")

    print(f"Todos os nós visitados na ordem: {visited}")
    return visited

# Exemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Inicia a BFS a partir do nó 'A'
bfs(graph, 'A')
