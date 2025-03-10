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

def custo_de(cidade1, cidade2, grafo):
    return grafo[cidade1].get(cidade2, float('inf'))

def tsp_dfs(origem, atual=None, cidades_visitadas=None, custo_atual=0, caminho_atual=None, melhor_custo=float('inf'), melhor_caminho=None, grafo=None):
    if atual is None:
        atual = origem
    if cidades_visitadas is None:
        cidades_visitadas = set([origem])
    if caminho_atual is None:
        caminho_atual = [origem]
    if melhor_caminho is None:
        melhor_caminho = []
    if grafo is None:
        raise ValueError("Grafo não fornecido")

    if len(cidades_visitadas) == len(grafo.vertices):
        custo_retorno = grafo.obter_custo(atual, origem)
        if custo_retorno == float('inf'):
            return melhor_custo, melhor_caminho
        custo_total = custo_atual + custo_retorno
        if custo_total < melhor_custo:
            melhor_custo = custo_total
            melhor_caminho = caminho_atual + [origem]
        return melhor_custo, melhor_caminho

    for vizinho, custo in grafo.vertices[atual].adjacentes:
        if vizinho not in cidades_visitadas:
            cidades_visitadas.add(vizinho)
            caminho_atual.append(vizinho)
            melhor_custo, melhor_caminho = tsp_dfs(origem, vizinho, cidades_visitadas, custo_atual + custo, caminho_atual, melhor_custo, melhor_caminho, grafo)
            cidades_visitadas.remove(vizinho)
            caminho_atual.pop()

    return melhor_custo, melhor_caminho