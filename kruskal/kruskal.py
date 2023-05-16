
class UnionFind:
    def __init__(self, size):
        self.parente = list(range(size))

    def encontrar(self, index):
        if self.parente[index] == index: return index
        self.parente[index] = self.encontrar(self.parente[index])
        return self.parente[index]

    def union(self, index1, index2):
        a, b = self.encontrar(index1), self.encontrar(index2)
        if a < b: a, b = b, a
        self.parente[b] = a

def kruskal(grafo):
    edges = sorted((cost, node, neighbor)
        for node, vizinhos in enumerate(grafo) 
        for neighbor, cost in vizinhos)

    sets = UnionFind(len(grafo))
    tree = []
    
    for cost, node1, node2 in edges:
        set1, set2 = sets.encontrar(node1), sets.encontrar(node2)
        if set1 == set2: continue
        sets.union(set1, set2)
        tree.append(((node1, node2), cost))
    return tree

grafo = [
    [(1, 5), (2, 15), (3, 16)],
    [(2, 13), (3, 1)],
    [(3, 1)],
    []
]

print(kruskal(grafo))