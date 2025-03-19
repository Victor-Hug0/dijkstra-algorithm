from min_heap import MinHeap
from dijkstra import dijkstra


graph = {
    'A': [('B', 2), ('C', 6)],
    'B': [('A', 2), ('C', 3), ('D', 5)],
    'C': [('A', 6), ('B', 3), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

origem = 'A' 
destino = 'D'
print(f"\nCaminho de {origem} para {destino}:")

dist, caminho = dijkstra(graph, origem, destino)

print(f"Distância: {dist}")
print(f"Rota: {caminho}")

h = MinHeap()
elementos = [[4, 'X'], [2, 'Y'], [7, 'Z'], [1, 'W'], [3, 'F'], [1, 'T']]

print("\nInserindo elementos:")
for e in elementos:
    h.insert(e)
    print(f"{e} => {h.heap}")

print("\nRemovendo elementos:")
while len(h.heap) > 0:
    min_e = h.pop_min()
    print(f"{min_e} => {h.heap if h.heap else '[[ ]]'}")

