import heapq
import math

# Step 1: Store driver locations
driver_locations = {
    "driver_1": (12.9611, 77.6387),
    "driver_2": (12.9612, 77.6400),
    "driver_3": (12.9620, 77.6390),
    "driver_4": (12.9650, 77.6350),
    "driver_5": (12.9580, 77.6410),
}


# Step 2: Distance calculation (Euclidean for simplicity)
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


# Step 3: Get N closest drivers
def get_closest_drivers(rider_location, n):
    max_heap = []

    for driver_id, driver_location in driver_locations.items():
        distance = calculate_distance(rider_location, driver_location)
        # Use -distance to simulate max-heap behavior
        if len(max_heap) < n:
            heapq.heappush(max_heap, (-distance, driver_id))
        else:
            if -distance > max_heap[0][0]:
                heapq.heappushpop(max_heap, (-distance, driver_id))

    # Return sorted list of closest drivers (closest first)
    return [driver_id for _, driver_id in sorted(max_heap, reverse=True)]


# Step 4: Test Example
rider = (12.9610, 77.6390)
closest_drivers = get_closest_drivers(rider, n=3)

# Output
print("Closest drivers to the rider:")
for driver in closest_drivers:
    print(driver)
