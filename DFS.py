def dfs_maior_custo(grafo, origem, destino, custo_atual, caminho_atual):
    visitados = []
    visitados.append(origem)
    
    if origem == destino:
        if custo_atual > dfs_maior_custo.custo_maximo:
            dfs_maior_custo.custo_maximo = custo_atual
            dfs_maior_custo.caminho_maximo = caminho_atual[:]
    
    for vizinho in grafo.vertices[origem].adjacentes:
        if vizinho not in visitados:
            dfs_maior_custo(grafo, vizinho, destino, custo_atual + grafo.vertices[origem].peso, caminho_atual + [vizinho])
    
    visitados.remove(origem)