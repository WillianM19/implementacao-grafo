import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []
        
    def __str__(self):
        content = f"Vertice: {self.nome}"
        
        if self.adjacentes:
            adjacentes_str = ", ".join([f"{v[0]}(peso={v[1]})" for v in self.adjacentes])
            content += f" | Adjacentes = {adjacentes_str}"
        
        return content

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
            
    def exibir_graficamente(self):
        G = nx.Graph()

        for vertice in self.vertices:
            G.add_node(vertice)

        for vertice in self.vertices:
            for adjacente, peso in self.vertices[vertice].adjacentes:
                G.add_edge(vertice, adjacente, weight=peso)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue")
        
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.show()


if __name__ == "__main__":
    grafo = Grafo()
    
    v1 = Vertice("v1")
    v2 = Vertice("v2")
    v3 = Vertice("v3")
    
    grafo.adicionar_vertice(v1)
    grafo.adicionar_vertice(v2)
    grafo.adicionar_vertice(v3)

    grafo.adicionar_aresta("v1", "v2")
    grafo.adicionar_aresta("v2", "v3")
    grafo.adicionar_aresta("v3", "v1")
    
    grafo.exibir_grafo()
    
    grafo.exibir_graficamente()
    

