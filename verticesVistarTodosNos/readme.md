# [Caminho mais curto visitando todos os nós](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)


Você tem um gráfico não direcionado e conectado de nnós rotulados de 0a n - 1. Você recebe uma matriz graphonde graph[i]está uma lista de todos os nós conectados com o nó ipor uma aresta.

Retorna o comprimento do caminho mais curto que visita cada nó . Você pode iniciar e parar em qualquer nó, pode revisitar os nós várias vezes e pode reutilizar arestas.


#
*Exemplo 1:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/07/07/untitled22.png)

Entrada: gráfico = [[1,2,3],[0],[0],[0]]
 Saída: 4
 Explicação: Um caminho possível é [1,0,2,0,3]

#
*Exemplo 2:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/07/07/untitled.png)

Entrada: gráfico = [[1],[0,2,4],[1,3,4],[2],[1,2]]
 Saída: 4
 Explicação: Um caminho possível é [0,1,4 ,2,3]

 #
 ## Restrições
-n == graph.length

-1 <= n <= 12

-0 <= graph[i].length < n

-graph[i]não contém i.

-Se graph[a]contém b, então graph[b]contém a.

-O gráfico de entrada está sempre conectado.