from dijkstra import dijkstra
from grafo import Grafo
import time

origem = input("Digite a origem: ")
destino = input("Digite o destino: ")

grafo = Grafo()
    
grafo.ler_csv("csv-dijkstra.csv")


inicio = time.time()
melhor_custo, melhor_caminho = dijkstra(grafo, origem, destino)
fim = time.time()
tempoExecucao1 =  fim - inicio

grafo.exibir_graficamente(melhor_caminho, melhor_custo)

print(f'Melhor Custo: {melhor_custo}')
print(f'Melhor Caminho: {melhor_caminho}')
print("Tempo de execução: {:.6f} segundos".format(tempoExecucao1))
