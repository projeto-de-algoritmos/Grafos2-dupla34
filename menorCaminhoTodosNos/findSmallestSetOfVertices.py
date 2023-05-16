def findSmallestSetOfVertices(n, edges):
    reachable = set(range(n))
    for edge in edges:
        reachable.discard(edge[1])  # Remove o vértice de chegada do conjunto de vértices alcançáveis
    return list(reachable)

# Exemplo 1
n1 = 6
edges1 = [[0,1],[0,2],[2,5],[3,4],[4,2]]
result1 = findSmallestSetOfVertices(n1, edges1)
print(result1)  # Saída: [0, 3]

# Exemplo 2
n2 = 5
edges2 = [[0,1],[2,1],[3,1],[1,4],[2,4]]
result2 = findSmallestSetOfVertices(n2, edges2)
print(result2)  # Saída: [0, 2, 3]