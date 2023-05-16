# [Número mínimo de vértices para alcançar todos os nós](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)


Dado um  grafo acíclico direcionado , com  n vértices numerados de  0 a  n-1, e um array  edges onde   representa uma aresta direcionada de nó   a nó  .edges[i] = [from_i, to_i]fromi toi

Encontre o menor conjunto de vértices a partir do qual todos os nós do grafo são alcançáveis . É garantido que existe uma solução única.

Observe que você pode retornar os vértices em qualquer ordem.


#
*Exemplo 1:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/07/07/untitled22.png)

Entrada: n = 6, arestas = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Saída: [0,3]

Saida: false

Explicação: Não há como particionar os nós em dois conjuntos independentes de forma que cada aresta conecte um nó em um e um nó no outro.
Example 2:
#
*Exemplo 2:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/07/07/untitled.png)

Entrada: n = 5, arestas = [[0,1],[2,1],[3,1],[1,4],[2,4]] 
Saída: [0,2,3]

Explicação: Observe que os vértices 0, 3 e 2 não são acessíveis de nenhum outro nó, portanto devemos incluí-los. Além disso, qualquer um desses vértices pode atingir os nós 1 e 4.