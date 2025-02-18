def BFS_saltos(grafo, origem, destino):
    visitados = []
    fila = []
    saltos = 0

    fila.append(origem)
    visitados.append(origem)
    
    while fila != []:
        tamanho_fila = len(fila)
        print(f"Tamanho da fila: {tamanho_fila}")
        
        for i in range(tamanho_fila):
            vertice_atual = fila.pop(0)
            
            if vertice_atual == destino:
                return len(visitados)
            
            for adjacente in grafo.vertices[vertice_atual].adjacentes:
                if adjacente not in visitados:
                    visitados.append(adjacente)
                    fila.append(adjacente)
        saltos += 1
        
    print("Numero total de saltos: ", saltos)
        
    return "Nenhum caminho encontrado"
