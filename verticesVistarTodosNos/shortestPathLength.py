from typing import List

def shortestPathLength(graph: List[List[int]]) -> int:
    n = len(graph)
    target = (1 << n) - 1  #estado de destino onde todos os nós foram visitados

    # # inicia o BFS de todos os nós simultaneamente
    q = [(i, 1 << i, 0) for i in range(n)]  # (node, state, distance)
    visited = set((i, 1 << i) for i in range(n))  # evite revisitar o mesmo nó com o mesmo estado

    while q:
        node, state, dist = q.pop(0)
        if state == target:
            return dist  # se todos os nós foram visitados, retorne a distância mais curta
        for neighbor in graph[node]:
            new_state = state | (1 << neighbor)  # marca vizinho como visitado
            if (neighbor, new_state) not in visited:
                visited.add((neighbor, new_state))
                q.append((neighbor, new_state, dist+1))
    
    return -1  #se não houver caminho que visite todos os nós, retorne -1

# Exemplo de uso:
graph = [[1,2,3],[0],[0],[0]]
print(shortestPathLength(graph))  # Saída: 4