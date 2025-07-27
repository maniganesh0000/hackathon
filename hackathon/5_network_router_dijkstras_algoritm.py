import heapq

# Step 1: Define the graph (adjacency list)
# Format: graph[node] = [(neighbor, cost), ...]
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1), ("E", 3)],
    "E": [("D", 3)],
}


# Step 2: Dijkstra’s Algorithm
def dijkstra(graph, source):
    heap = [(0, source)]  # (cost, node)
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    visited = set()

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_cost = current_cost + weight
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))

    return distances


# Step 3: Run and print
source_node = "A"
shortest_paths = dijkstra(graph, source_node)

print(f"Shortest paths from {source_node}:")
for node, cost in shortest_paths.items():
    print(f"{node}: {cost}")
