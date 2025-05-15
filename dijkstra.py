from min_heap import MinHeap

def dijkstra(graph, start, end):
    
    num_nodes = len(graph)
    if start < 0 or start >= num_nodes or end < 0 or end >= num_nodes:
        raise RuntimeError("Nós inválidos!")
    
    minHeap = MinHeap()
    minHeap.insert([0, start])
    processed = set()
    
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    
    previous = [None] * num_nodes
    
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
