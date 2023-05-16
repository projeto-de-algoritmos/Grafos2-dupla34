
def dijkstra(grafo, inicio, fim):
    # Inicializa os valores dos vértices
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    visitados = set()
    nao_visitados = set(grafo.keys())

    while nao_visitados:
        # Seleciona o vértice não visitado com menor distância
        atual = min(nao_visitados, key=lambda vertice: distancias[vertice])

        # Verifica se chegou ao fim
        if atual == fim:
            return distancias[fim]

        # Atualiza a distância para cada vizinho do vértice atual
        for vizinho, peso in grafo[atual].items():
            if vizinho in visitados:
                continue
            nova_distancia = distancias[atual] + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia

        # Marca o vértice atual como visitado
        visitados.add(atual)
        nao_visitados.remove(atual)

    # Se não há caminho entre o início e o fim, retorna None
    return None


grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 4},
    'C': {'A': 3, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

inicio = 'A'
fim = 'D'
distancia_minima = dijkstra(grafo, inicio, fim)
print(distancia_minima)