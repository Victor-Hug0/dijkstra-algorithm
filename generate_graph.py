def generate_graph(target_size, avg_degree):
    import random
    
    grafo = {"A": []}  # Inicializa grafo como lista de adjacência
    nodes = ["A"]
    total_edges = 0
    
    # Máximo de tentativas para adicionar arestas
    max_attempts = 100
    
    while len(nodes) < target_size:
        source = random.choice(nodes)
        new_node = chr(65 + len(nodes)) if len(nodes) < 26 else str(len(nodes))
        
        if new_node not in grafo:
            grafo[new_node] = []
        
        # Adicionar aresta base
        peso = random.randint(1, 10)
        grafo[source].append((new_node, peso))
        grafo[new_node].append((source, peso))
        total_edges += 1
        
        # Calcular arestas necessárias após adicionar o novo nó
        target_edges = (len(nodes) + 1) * avg_degree // 2
        remaining_edges = target_edges - total_edges
        
        # Adicionar arestas adicionais de forma mais eficiente
        attempts = 0
        while total_edges < target_edges and attempts < max_attempts:
            u = random.choice(nodes)
            v = random.choice(nodes)
            if u != v and all(neighbor != v for neighbor, _ in grafo[u]):
                peso = random.randint(1, 10)
                grafo[u].append((v, peso))
                grafo[v].append((u, peso))
                total_edges += 1
            attempts += 1
        
        nodes.append(new_node)
    
    return grafo
