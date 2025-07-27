import heapq

# Step 1: Define the market graph
# Format: 'A': [('B', rate), ...]
market_graph = {
    "A": [("B", 1.2), ("C", 0.8)],
    "B": [("C", 1.5), ("A", 0.9)],
    "C": [("A", 1.3), ("B", 0.7)],
}


# Step 2: Modified Dijkstra's using max-product path
def find_best_trade_loop(start_market):
    heap = [(-1.0, start_market, [start_market])]  # (-profit, current, path)
    visited = {}

    while heap:
        neg_profit, current, path = heapq.heappop(heap)
        profit = -neg_profit

        # Check for a profitable loop
        if current == start_market and len(path) > 1:
            return path, profit

        # Avoid revisiting worse paths to same node
        if current in visited and visited[current] >= profit:
            continue
        visited[current] = profit

        for neighbor, rate in market_graph.get(current, []):
            if neighbor == start_market and len(path) == 1:
                continue  # skip 1-hop back to start
            new_profit = profit * rate
            heapq.heappush(heap, (-new_profit, neighbor, path + [neighbor]))

    return None, 0.0


# Step 3: Run it
start = "A"
loop_path, max_profit = find_best_trade_loop(start)

# Step 4: Output
if loop_path:
    print(f"Most profitable trade loop: {' -> '.join(loop_path)} -> {start}")
    print(f"Final profit multiplier: {max_profit:.4f}")
else:
    print("No profitable trade loop found.")
