from min_heap import MinHeap

def dijkstra(graph, start, end):
    
    if start not in graph or end not in graph or start == end:
        raise RuntimeError("Valores incorretos passados como parâmetro!")
    
    minHeap = MinHeap()
    minHeap.insert([0, start])
    processed = set()
    
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    
    previous = {node: None for node in graph}
    
    while len(minHeap.heap) > 0:
        current_distance, current_node = minHeap.pop_min()
                
        if current_node == end:
            break
        
        if current_node in processed:
            continue
        
        processed.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            if neighbor in processed:
                continue
            
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                minHeap.insert([distance, neighbor])
                
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
            
    return distances[end], path 
