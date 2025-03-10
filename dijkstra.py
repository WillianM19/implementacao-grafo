
class MinHeap:
    def __init__(self, capacity=100):
        self.array = [None] * (capacity + 1)  
        self.size = 0  

    def insert(self, elemento):
        if self.size >= len(self.array) - 1:
            print("Overflow: A heap está cheia.")
            return

        self.size += 1
        self.array[self.size] = elemento
        self._subir(self.size)

    def extract_min(self):
        if self.size == 0:
            print("Underflow: A heap está vazia.")
            return None

        raiz = self.array[1]  
        self.array[1] = self.array[self.size]  
        self.array[self.size] = None  
        self.size -= 1

        self._descer(1)
        return raiz  

    def get_min(self):
        return self.array[1] if self.size > 0 else None

    def is_empty(self):
        return self.size == 0

    def _subir(self, i):
        pai = i // 2
        if pai >= 1 and self.array[i] < self.array[pai]:
            self.array[i], self.array[pai] = self.array[pai], self.array[i]
            self._subir(pai)

    def _descer(self, i):
        menor = i
        esquerda = 2 * i
        direita = 2 * i + 1

        if esquerda <= self.size and self.array[esquerda] < self.array[menor]:
            menor = esquerda

        if direita <= self.size and self.array[direita] < self.array[menor]:
            menor = direita

        if menor != i:
            self.array[i], self.array[menor] = self.array[menor], self.array[i]
            self._descer(menor)


def dijkstra(grafo, origem, destino):
    distancias = {vertice: float('inf') for vertice in grafo.vertices}
    predecessores = {vertice: None for vertice in grafo.vertices}
    distancias[origem] = 0

    heap = MinHeap()
    heap.insert((0, origem))

    while not heap.is_empty():
        distancia_atual, vertice_atual = heap.extract_min()

        if vertice_atual == destino:
            melhor_caminho = []
            while vertice_atual:
                melhor_caminho.insert(0, vertice_atual)
                vertice_atual = predecessores[vertice_atual]
            melhor_custo = distancias[destino]
            return melhor_custo, melhor_caminho

        for adjacente, peso in grafo.vertices[vertice_atual].adjacentes:
            distancia = distancia_atual + peso
            if distancia < distancias[adjacente]:
                distancias[adjacente] = distancia
                predecessores[adjacente] = vertice_atual
                heap.insert((distancia, adjacente))

    return float('inf'), []
