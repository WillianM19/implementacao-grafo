"""
Implemente um sistema de rotas de transporte em que cada cidade é um vértice e as estradas são arestas ponderadas.
Use BFS para encontrar o caminho com menor número de paradas entre duas cidades.
"""

from BFS import BFS_saltos
from grafo import Grafo, Vertice

# Montando Sistema de rotas de trasporte
rotas = Grafo()
    
cidade1 = Vertice("cidade1", 5)
cidade2 = Vertice("cidade2", 6)
cidade3 = Vertice("cidade3", 7)

rotas.adicionar_vertice(cidade1)
rotas.adicionar_vertice(cidade2)
rotas.adicionar_vertice(cidade3)

rotas.adicionar_aresta("cidade1", "cidade2")
rotas.adicionar_aresta("cidade2", "cidade3")
rotas.adicionar_aresta("cidade3", "cidade1")

rotas.exibir_graficamente()

# Executando BFS
resultado = BFS_saltos(rotas, "cidade1", "cidade2")
print(resultado)