from BFS import bfs_menor_custo
from DFS import dfs_maior_custo, tsp_dfs
from grafo import Grafo, Vertice

# Montando Sistema de rotas de trasporte
grafo = Grafo()
    
grafo.ler_csv("csv_grafo.csv")

melhor_custo, melhor_caminho = tsp_dfs("A", grafo=grafo)

grafo.exibir_graficamente(melhor_caminho, melhor_custo)

print(f'Melhor Custo: {melhor_custo}')
print(f'Melhor Caminho: {melhor_caminho}')

