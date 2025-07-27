import heapq

# Step 1: Define the recipe book and base costs
recipes = {
    "metal_plate": {"needs": {"iron_ore": 3}, "time": 5},
    "magic_dust": {"needs": {"crystal": 2}, "time": 7},
    "philosopher_stone": {"needs": {"metal_plate": 2, "magic_dust": 4}, "time": 20},
}

base_costs = {"iron_ore": 10, "crystal": 25}

# Step 2: Reverse dependency graph
reverse_deps = {}
for item, recipe in recipes.items():
    for ingredient in recipe["needs"]:
        reverse_deps.setdefault(ingredient, []).append(item)

# Step 3: Initialize
min_cost = dict(base_costs)  # Items and their known minimum cost
heap = [(cost, item) for item, cost in base_costs.items()]
heapq.heapify(heap)

# Track how many ingredients are needed for each item
waiting = {}
needed_qty = {}

for item, recipe in recipes.items():
    waiting[item] = set(recipe["needs"])
    needed_qty[item] = recipe["needs"]

# Step 4: Crafting loop (Dijkstra-style traversal)
while heap:
    current_cost, item = heapq.heappop(heap)

    if item not in reverse_deps:
        continue

    for target in reverse_deps[item]:
        waiting[target].discard(item)

        if not waiting[target]:  # All ingredients ready
            total = recipes[target]["time"]
            for ingr, qty in needed_qty[target].items():
                total += min_cost[ingr] * qty
            if target not in min_cost or total < min_cost[target]:
                min_cost[target] = total
                heapq.heappush(heap, (total, target))

# Step 5: Print final result
target_item = "philosopher_stone"
if target_item in min_cost:
    print(f"Minimum cost to craft '{target_item}': {min_cost[target_item]}")
else:
    print(f"Cannot craft {target_item} with the given recipes.")
