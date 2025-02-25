def bfs_menor_custo(grafo, origem, destino):
    visitados = []
    fila = []
    saltos = 0

    fila.append(origem)
    visitados.append(origem)
    
    while fila != []:
        tamanho_fila = len(fila)
        
        for i in range(tamanho_fila):
            vertice_atual = fila.pop(0)
            
            if vertice_atual == destino:
                return saltos
            
            for adjacente in grafo.vertices[vertice_atual].adjacentes:
                if adjacente not in visitados:
                    visitados.append(adjacente)
                    fila.append(adjacente)
        
        saltos += 1
    
    return "Nenhum caminho encontrado"
