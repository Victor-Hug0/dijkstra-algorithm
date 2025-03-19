from dijkstra_bm import dijkstra
from generate_graph import generate_graph
import time
import gc

def benchmark(gaphLen):
    results = []
    
    for n in range(len(gaphLen)):
        gc.collect()
        graph = generate_graph(gaphLen[n], 5)
        nodes = list(graph.keys())
        start_node = nodes[0]
        end_node = nodes[-1]
        start = time.time()
        dijkstra(graph, start_node, end_node)
        end = time.time()
        total = end-start
        
        print(f"{gaphLen[n]} -> {total} ms")
        
        results.append((n, total))
        
        del graph
        gc.collect()
        
    return results
        

start_value = 32000
end_value = 4096000
graphLenght = []

while start_value <= end_value:
    graphLenght.append(start_value)
    start_value *= 2

results = benchmark(graphLenght)
