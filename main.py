from DFS import tsp_dfs
from grafo import Grafo
import time

# Grafo 1
grafo = Grafo()
    
grafo.ler_csv("forca-bruta-1.csv")

inicio = time.time()
melhor_custo, melhor_caminho = tsp_dfs("1", grafo=grafo)
fim = time.time()
tempoExecucao1 =  fim - inicio

grafo.exibir_graficamente(melhor_caminho, melhor_custo)

print("\nGrafo 1:")
print(f'Melhor Custo: {melhor_custo}')
print(f'Melhor Caminho: {melhor_caminho}')
print("Tempo de execução: {:.5f} segundos".format(tempoExecucao1))

# Grafo 2
grafo2 = Grafo()
grafo2.ler_csv("forca-bruta-2.csv")

melhor_custo, melhor_caminho = tsp_dfs("1", grafo=grafo2)

inicio = time.time()
grafo2.exibir_graficamente(melhor_caminho, melhor_custo)
fim = time.time()
tempoExecucao2 =  fim - inicio

print("\nGrafo 2:")
print(f'Melhor Custo: {melhor_custo}')
print(f'Melhor Caminho: {melhor_caminho}')
print("Tempo de execução: {:.5f} segundos".format(tempoExecucao2))

