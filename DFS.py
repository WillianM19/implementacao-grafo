def dfs_maior_custo(grafo, origem, destino, custo_atual, caminho_atual):
    visitados = set()
    visitados.add(origem)
    
    if origem == destino:
        return custo_atual, caminho_atual
    
    custo_maximo = 0
    caminho_maximo = []
    
    for vizinho in grafo.vertices[origem].adjacentes:
        if vizinho not in visitados:
            visitados.add(vizinho)
            custo_temp, caminho_temp = dfs_maior_custo(
                grafo, vizinho, destino, custo_atual + grafo.vertices[origem].peso, caminho_atual + [vizinho]
            )
            
            # Atualiza o custo máximo e o caminho máximo
            if custo_temp > custo_maximo:
                custo_maximo = custo_temp
                caminho_maximo = caminho_temp
    visitados.remove(vizinho)

    return custo_maximo, caminho_maximo
