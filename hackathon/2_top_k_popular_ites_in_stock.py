import heapq

# Step 1: Initialize data
request_counts = {}  # {item_id: count}
stock_levels = {}  # {item_id: stock}


# Step 2: Function to request an item
def request_item(item_id):
    if item_id in stock_levels and stock_levels[item_id] > 0:
        request_counts[item_id] = request_counts.get(item_id, 0) + 1
        print(f"Request accepted for {item_id}")
    else:
        print(f"Request rejected: {item_id} is out of stock or unknown.")


# Step 3: Function to restock items
def restock_item(item_id, quantity):
    stock_levels[item_id] = stock_levels.get(item_id, 0) + quantity
    print(f"Restocked {item_id}: New stock = {stock_levels[item_id]}")


# Step 4: Get top K popular in-stock items
def get_top_k_items(k):
    min_heap = []

    for item_id, count in request_counts.items():
        if stock_levels.get(item_id, 0) > 0:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, item_id))
            else:
                if count > min_heap[0][0]:
                    heapq.heappushpop(min_heap, (count, item_id))

    # Return sorted result by count descending
    return sorted(min_heap, reverse=True)


# Step 5: Simulate Usage
restock_item("item1", 10)
restock_item("item2", 5)
restock_item("item3", 0)
restock_item("item4", 2)

request_item("item1")
request_item("item1")
request_item("item2")
request_item("item2")
request_item("item2")
request_item("item4")
request_item("item3")  # Should be rejected
request_item("item1")
request_item("item2")
request_item("item4")
request_item("item4")  # Should be rejected if stock exhausted

# Step 6: Get Top 2
top_k = get_top_k_items(k=2)
print("\nTop K Popular In-Stock Items:")
for count, item_id in top_k:
    print(f"{item_id}: {count} requests")
