import random
import time
import threading

# Tracking counters
stats = {"processed": 0, "impounded": 0, "north": 0, "south": 0}
lock = threading.Lock()

"""
This script simulates a post office processing letters using threads.
The threading is quite neat but requires careful management of shared state. It is also
possible to overwhelm the cpu. 
NOTE that multiple threads can be ran because the sleep is like I/O bound, not CPU bound.
So it relaxes the CPU and allows other threads to run.
For CPU bound tasks, you would use multiprocessing."""


def sort(address):
    random_number = random.random()
    if random_number < 0.5:
        time.sleep(1)  # Coffee break
    if address % 2 == 0:
        return "south"
    return "north"


def check(letter):
    random_number = random.random()
    if random_number < 0.5:
        return True
    return False


letters = [{"name": f"Person {i}", "address": i} for i in range(1, 101)]

# lets generate a bunch of letters


def process_letter(letter):
    if check(letter):
        print(f"Processing letter for {letter['name']} at {letter['address']}")
        direction = sort(letter["address"])
        with lock:
            stats["processed"] += 1
            stats[direction] += 1
        print(f"Letter will be sent to the {direction} sub-office.")
    else:
        print(f"Impounding letter for {letter['name']} at {letter['address']}")
        with lock:
            stats["impounded"] += 1


threads = []

for letter in letters:
    thread = threading.Thread(target=process_letter, args=(letter,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
print("All letters processed.")

# Print final stats
print("\n📬 Final Stats:")
for key, value in stats.items():
    print(f"{key.capitalize()}: {value}")
