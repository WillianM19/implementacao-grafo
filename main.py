from BFS import bfs_menor_custo
from DFS import dfs_maior_custo, tsp_dfs
from grafo import Grafo, Vertice

# Grafo 1
grafo = Grafo()
    
grafo.ler_csv("forca-bruta-1.csv")

melhor_custo, melhor_caminho = tsp_dfs("1", grafo=grafo)
grafo.exibir_graficamente(melhor_caminho, melhor_custo)

print("\nGrafo 1:")
print(f'Melhor Custo: {melhor_custo}')
print(f'Melhor Caminho: {melhor_caminho}')

# Grafo 2
grafo2 = Grafo()
grafo2.ler_csv("forca-bruta-2.csv")

melhor_custo, melhor_caminho = tsp_dfs("1", grafo=grafo2)
grafo2.exibir_graficamente(melhor_caminho, melhor_custo)

print("\nGrafo 2:")
print(f'Melhor Custo: {melhor_custo}')
print(f'Melhor Caminho: {melhor_caminho}')

