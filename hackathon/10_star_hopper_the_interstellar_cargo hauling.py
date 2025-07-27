import heapq

# Step 1: Define the graph (planet connectivity with fuel cost)
graph = {
    "Home": [("A", 5), ("B", 10)],
    "A": [("B", 2), ("C", 4), ("Home", 5)],
    "B": [("A", 2), ("C", 3), ("Home", 10)],
    "C": [("A", 4), ("B", 3), ("Home", 7)],
}

# Step 2: Define contracts (pickup, dropoff)
contracts = [("A", "C"), ("B", "C")]
n_contracts = len(contracts)
contract_map = {i: {"pickup": p, "dropoff": d} for i, (p, d) in enumerate(contracts)}

# Bitmask: 0..2n-1 => pickup & dropoff bits for each contract
# 2 bits per contract: bit 2*i => pickup, bit 2*i+1 => dropoff
all_delivered_mask = (1 << (2 * n_contracts)) - 1


# Step 3: A* Search Function
def a_star_cargo_route(start):
    heap = [(0, start, 0)]  # (fuel_cost, current_planet, delivery_mask)
    visited = {}

    while heap:
        cost, current, mask = heapq.heappop(heap)

        if (current, mask) in visited and visited[(current, mask)] <= cost:
            continue
        visited[(current, mask)] = cost

        # Goal check: all contracts completed and back at Home
        if mask == all_delivered_mask and current == start:
            return cost

        # Consider moving to neighbors
        for neighbor, fuel in graph[current]:
            new_mask = mask

            for i, contract in contract_map.items():
                pickup_bit = 1 << (2 * i)
                dropoff_bit = 1 << (2 * i + 1)

                # Pickup
                if current == contract["pickup"] and not (mask & pickup_bit):
                    if neighbor != contract["dropoff"]:  # prevent immediate drop
                        new_mask |= pickup_bit

                # Dropoff
                if (
                    current == contract["dropoff"]
                    and (mask & pickup_bit)
                    and not (mask & dropoff_bit)
                ):
                    new_mask |= dropoff_bit

            heapq.heappush(heap, (cost + fuel, neighbor, new_mask))

    return float("inf")  # No valid route found


# Step 4: Run the search
min_cost = a_star_cargo_route("Home")
print(f"Minimum fuel to complete all deliveries and return home: {min_cost}")
