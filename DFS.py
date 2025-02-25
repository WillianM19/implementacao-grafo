def dfs_maior_custo(grafo, origem, destino, caminho_atual=None, custo_atual=0, visitados=None):
    # Inicia caminho inicial na origem
    if caminho_atual is None:
        caminho_atual = [origem]
    
    # Inicia visitados como um set vazio
    if visitados is None:
        visitados = set()
    
    visitados.add(origem)
    
    # Condição de parada
    if origem == destino:
        return custo_atual, caminho_atual
    
    custo_maximo = custo_atual
    caminho_maximo = caminho_atual
    
    for vizinho, peso in grafo.vertices[origem].adjacentes:
        if vizinho not in visitados:
            custo_temp, caminho_temp = dfs_maior_custo(
                grafo, vizinho, destino, caminho_atual + [vizinho], custo_atual + peso, visitados
            )
            
            # Atualiza o custo máximo e o caminho máximo
            if custo_temp > custo_maximo:
                custo_maximo = custo_temp
                caminho_maximo = caminho_temp
    
    visitados.remove(origem)
    return custo_maximo, caminho_maximo
