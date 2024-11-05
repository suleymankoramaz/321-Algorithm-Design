def findMinLatency(graph, source, destination):
    
    def dfs(current_node, current_path, current_latency):
        nonlocal min_latency, best_path

        if current_node == destination:
            if current_latency < min_latency:
                min_latency = current_latency
                best_path = current_path.copy()
            return

        for neighbor, edge_latency in graph[current_node]:
            if neighbor not in current_path:
                dfs(neighbor, current_path + [neighbor], current_latency + edge_latency)

    min_latency = float('inf')
    best_path = []

    dfs(source, [source], 0)

    return best_path, min_latency