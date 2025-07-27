import heapq


# Step 1: Function to compute max overlap between two strings
def compute_overlap(a, b):
    max_len = min(len(a), len(b))
    for i in range(max_len, 0, -1):
        if a[-i:] == b[:i]:
            return i
    return 0


# Step 2: Initialize fragments
initial_fragments = ["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC"]

# Step 3: Assign fragment IDs and make dict
fragments = {i: frag for i, frag in enumerate(initial_fragments)}
active_ids = set(fragments.keys())

# Step 4: Build initial heap of all overlaps
heap = []
for id1 in fragments:
    for id2 in fragments:
        if id1 != id2:
            overlap = compute_overlap(fragments[id1], fragments[id2])
            if overlap > 0:
                heapq.heappush(heap, (-overlap, id1, id2))  # max-heap via negative

# Step 5: Merge loop
next_id = max(fragments) + 1
while len(active_ids) > 1:
    while heap:
        neg_overlap, id1, id2 = heapq.heappop(heap)
        if id1 in active_ids and id2 in active_ids:
            break
    else:
        break  # No valid overlaps left

    # Merge id1 and id2
    merged_seq = fragments[id1] + fragments[id2][abs(neg_overlap) :]
    fragments[next_id] = merged_seq
    active_ids.remove(id1)
    active_ids.remove(id2)
    active_ids.add(next_id)

    # Add new overlaps to heap
    for other_id in active_ids:
        if other_id == next_id:
            continue
        # next_id → other
        overlap1 = compute_overlap(fragments[next_id], fragments[other_id])
        if overlap1 > 0:
            heapq.heappush(heap, (-overlap1, next_id, other_id))
        # other → next_id
        overlap2 = compute_overlap(fragments[other_id], fragments[next_id])
        if overlap2 > 0:
            heapq.heappush(heap, (-overlap2, other_id, next_id))

    next_id += 1

# Step 6: Print final sequence
final_sequence = fragments[active_ids.pop()]
print("Final reconstructed DNA sequence:")
print(final_sequence)
