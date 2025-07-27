import heapq
import itertools

# Global data structures
patient_heap = []  # (urgency, count, name) -> min-heap
entry_finder = {}  # name -> entry
REMOVED = "<REMOVED>"  # Marker for removed entries
counter = itertools.count()  # Unique sequence count to avoid heap tie


# Step 1: Add a patient
def add_patient(name, urgency):
    if name in entry_finder:
        update_patient(name, urgency)
        return
    count = next(counter)
    entry = [urgency, count, name]
    entry_finder[name] = entry
    heapq.heappush(patient_heap, entry)
    print(f"Patient {name} added with urgency {urgency}.")


# Step 2: Call the most urgent patient
def call_next_patient():
    while patient_heap:
        urgency, count, name = heapq.heappop(patient_heap)
        if name != REMOVED:
            del entry_finder[name]
            print(f"Calling patient: {name} (urgency: {urgency})")
            return name
    print("No patients in the queue.")
    return None


# Step 3: Update patient's urgency
def update_patient(name, new_urgency):
    old_entry = entry_finder.get(name)
    if old_entry:
        old_entry[2] = REMOVED  # Mark old entry as removed
    count = next(counter)
    new_entry = [new_urgency, count, name]
    entry_finder[name] = new_entry
    heapq.heappush(patient_heap, new_entry)
    print(f"Patient {name}'s urgency updated to {new_urgency}.")


# Step 4: Print current valid patients
def print_patients():
    print("Current queue (valid entries):")
    for urgency, count, name in patient_heap:
        if name != REMOVED:
            print(f"{name} - urgency {urgency}")
    print()


# --- Example usage ---

add_patient("Alice", 4)
add_patient("Bob", 2)
add_patient("Charlie", 5)
add_patient("Daisy", 3)
print_patients()

update_patient("Alice", 1)
print_patients()

call_next_patient()  # Should call Alice
call_next_patient()  # Then Bob
print_patients()
