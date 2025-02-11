import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []
        
    def __str__(self):
        content = f"{self.nome}"
        
        if (self.adjacentes):
            content = f"Vertice: {content} | Adjacentes =  {", ".join(self.adjacentes)}"
        
        return str(content)

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
    
    def adicionar_aresta(self, vertice1, vertice2):
            if vertice1 in self.vertices and vertice2 in self.vertices:
                self.vertices[vertice1].adjacentes.append(vertice2)
                self.vertices[vertice2].adjacentes.append(vertice1)
        
    def exibir_grafo(self):
        for vertice in list(self.vertices):
            print(self.vertices[vertice])
            
    def exibir_graficamente(self):
        G = nx.Graph()

        for vertice in self.vertices:
            G.add_node(vertice)

        for vertice in self.vertices:
            for adjacente in self.vertices[vertice].adjacentes:
                G.add_edge(vertice, adjacente)

        nx.draw(G, with_labels=True)
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
    

