"""
Implemente um sistema de rotas de transporte em que cada cidade é um vértice e as estradas são arestas ponderadas.
Use BFS para encontrar o caminho com menor número de paradas entre duas cidades.
"""

from BFS import bfs_menor_custo
from DFS import dfs_maior_custo
from grafo import Grafo, Vertice

# Montando Sistema de rotas de trasporte
rotas = Grafo()
    
cidade1 = Vertice("cidade1")
cidade2 = Vertice("cidade2")
cidade3 = Vertice("cidade3")
cidade4 = Vertice("cidade4")
cidade5 = Vertice("cidade5")

rotas.adicionar_vertice(cidade1)
rotas.adicionar_vertice(cidade2)
rotas.adicionar_vertice(cidade3)
rotas.adicionar_vertice(cidade4)
rotas.adicionar_vertice(cidade5)

rotas.adicionar_aresta("cidade1", "cidade2", 5)
rotas.adicionar_aresta("cidade2", "cidade3", 3)
rotas.adicionar_aresta("cidade1", "cidade3", 7)
rotas.adicionar_aresta("cidade3", "cidade4", 2)
rotas.adicionar_aresta("cidade1", "cidade5", 9)


rotas.exibir_graficamente()

print("Viagem de cidade1 para cidade4:\n")

# Executando BFS (Menor custo)
resultado = bfs_menor_custo(rotas, "cidade1", "cidade4")
print("Resultado BFS (Caminho com menor número de paradas):", resultado) # 2

# Executando DFS (Maior custo)
resultado = dfs_maior_custo(rotas, "cidade1", "cidade4")
print("Resultado DFS (Caminho com maior custo em peso arestas):", resultado[0]) # 10

# Lendo arquivo csv
grafo_csv = Grafo()

print("Lendo arquivo csv...\n")
grafo_csv.ler_csv("csv_grafo.csv")

grafo_csv.exibir_graficamente()