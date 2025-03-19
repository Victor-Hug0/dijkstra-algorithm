import min_heap

def dijkstra(graph, start, end):
    
    if start not in graph or end not in graph or start == end:
        raise RuntimeError("Valores incorretos passados como parâmetro!")
    
    minHeap = min_heap.MinHeap()
    minHeap.insert([0, start])
    
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    
    while len(minHeap.heap) > 0:
        current_distance, current_node = minHeap.pop_min()
        
        if current_node == end:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                minHeap.insert([distance, neighbor])
                          
    return distances[end]
