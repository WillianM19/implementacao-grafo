import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []
        
    def __str__(self):
        content = f"Vertice: {self.nome}"
        
        if (self.adjacentes):
            content = f"Vertice: {content} | Adjacentes =  {", ".join(self.adjacentes)}"
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
            
            for adjacente, peso in grafo.vertices[vertice_atual].adjacentes:
                if adjacente not in visitados:
                    visitados.append(adjacente)
                    fila.append(adjacente)
        
        saltos += 1
    
    return "Nenhum caminho encontrado"
class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
    
    def adicionar_aresta(self, vertice1, vertice2, peso=1):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].adjacentes.append((vertice2, peso))
            self.vertices[vertice2].adjacentes.append((vertice1, peso))
        
    def exibir_grafo(self):
        for vertice in self.vertices.values():
            print(vertice)
            
    def exibir_graficamente(self, caminho=None):
        G = nx.Graph()

        for vertice in self.vertices:
            G.add_node(vertice)

        for vertice in self.vertices:
            for adjacente, peso in self.vertices[vertice].adjacentes:
                G.add_edge(vertice, adjacente, weight=peso)

        pos = nx.spring_layout(G)
        fig, ax = plt.subplots(figsize=(8, 8))

        def update(num, nodes, edges, ax):
            ax.clear()

            if caminho:
                caminho_edges = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
                subgraph_nodes = set(caminho)
                subgraph_edges = [(u, v) for u, v in G.edges() if (u, v) in caminho_edges or (v, u) in caminho_edges]

                nx.draw_networkx_nodes(G, pos, nodelist=subgraph_nodes, node_size=1000, node_color="lightgreen", ax=ax)
                nx.draw_networkx_labels(G, pos, labels={n: n for n in subgraph_nodes}, ax=ax)
                nx.draw_networkx_edges(G, pos, edgelist=subgraph_edges, edge_color="red", width=2, ax=ax)

                edge_labels = {(u, v): G[u][v]['weight'] for u, v in subgraph_edges}
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

                plt.title("Caminho Específico")
            else:
                if num < len(nodes):
                    nx.draw_networkx_nodes(G, pos, nodelist=nodes[:num + 1], node_size=1000, node_color="lightblue", ax=ax)
                    nx.draw_networkx_labels(G, pos, labels={n: n for n in nodes[:num + 1]}, ax=ax)
                    plt.title(f"Adicionando vértices: Passo {num + 1}")
                else:
                    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_size=1000, node_color="lightblue", ax=ax)
                    nx.draw_networkx_labels(G, pos, ax=ax)

                    edge_index = num - len(nodes)
                    if edge_index < len(edges):
                        nx.draw_networkx_edges(G, pos, edgelist=edges[:edge_index + 1], ax=ax)

                        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True) if (u, v) in edges[:edge_index + 1]}
                        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
                        plt.title(f"Adicionando arestas: Passo {edge_index + 1}")

        nodes = list(G.nodes())
        edges = list(G.edges())

        ani = animation.FuncAnimation(
            fig, update,
            frames=len(nodes) + len(edges),
            fargs=(nodes, edges, ax),
            interval=200,
            repeat=False
        )
        plt.show()
    
    def ler_csv(self, arquivo_csv):
        with open(arquivo_csv, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for linha in csv_reader:
                origem = linha['Origem']
                destino = linha['Destino']
                peso = int(linha['Peso'])
                
                if origem not in self.vertices:
                    self.adicionar_vertice(Vertice(origem))
                
                if destino not in self.vertices:
                    self.adicionar_vertice(Vertice(destino))
                
                self.adicionar_aresta(origem, destino, peso)

    def obter_custo(self, vertice1, vertice2):
            if vertice1 in self.vertices and vertice2 in self.vertices:
                for adj, peso in self.vertices[vertice1].adjacentes:
                    if adj == vertice2:
                        return peso
            return float('inf')

if __name__ == "__main__":
    grafo = Grafo()
    
    v1 = Vertice("v1")
    v2 = Vertice("v2")
    v3 = Vertice("v3")
    v4 = Vertice("v4")
    
    grafo.adicionar_vertice(v1)
    grafo.adicionar_vertice(v2)
    grafo.adicionar_vertice(v3)
    grafo.adicionar_vertice(v4)

    grafo.adicionar_aresta("v1", "v2")
    grafo.adicionar_aresta("v2", "v3")
    grafo.adicionar_aresta("v2", "v4")
    grafo.adicionar_aresta("v3", "v4")
    grafo.adicionar_aresta("v4", "v1")
    
    grafo.exibir_grafo()
    
    grafo.exibir_graficamente()
    

