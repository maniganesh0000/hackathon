import heapq

# Constants
COOLDOWN_TIME = 5  # seconds between light changes
PROCESS_TIME = 1  # seconds to process a car

# Initial event queue (timestamp, event_type, event_data)
event_queue = [
    (1, "CAR_ARRIVAL", {"intersection": "A", "direction": "N"}),
    (2, "CAR_ARRIVAL", {"intersection": "A", "direction": "S"}),
    (3, "CAR_ARRIVAL", {"intersection": "A", "direction": "E"}),
    (4, "CAR_ARRIVAL", {"intersection": "A", "direction": "W"}),
    (6, "CAR_ARRIVAL", {"intersection": "A", "direction": "E"}),
]

# Step 1: Initialize intersection states
intersections = {
    "A": {
        "light": "GREEN_NS",
        "next_change": 10,  # scheduled change
        "queues": {"N": [], "S": [], "E": [], "W": []},
    }
}

# Step 2: Seed initial light change event
heapq.heappush(event_queue, (10, "CHANGE_LIGHT", {"intersection": "A"}))

# Step 3: Main simulation loop
while event_queue:
    timestamp, event_type, data = heapq.heappop(event_queue)
    inter_id = data["intersection"]
    intersection = intersections[inter_id]

    if event_type == "CAR_ARRIVAL":
        direction = data["direction"]
        intersection["queues"][direction].append(timestamp)
        print(f"[{timestamp}] Car arrived at {inter_id} from {direction}")

    elif event_type == "CHANGE_LIGHT":
        current_light = intersection["light"]
        new_light = "GREEN_EW" if current_light == "GREEN_NS" else "GREEN_NS"
        intersection["light"] = new_light
        print(f"[{timestamp}] Light at {inter_id} changed to {new_light}")

        # Process cars in green directions
        green_dirs = ["N", "S"] if new_light == "GREEN_NS" else ["E", "W"]
        for dir in green_dirs:
            queue = intersection["queues"][dir]
            if queue:
                car_time = queue.pop(0)
                wait_time = timestamp - car_time
                print(
                    f"[{timestamp}] Car from {dir} passed at {inter_id} (waited {wait_time}s)"
                )
                # process one car only
                break

        # Schedule next light change
        next_time = timestamp + COOLDOWN_TIME
        intersection["next_change"] = next_time
        heapq.heappush(
            event_queue, (next_time, "CHANGE_LIGHT", {"intersection": inter_id})
        )
