import random
import time


def sort(address):
    random_number = random.random()
    if random_number < 0.5:
        time.sleep(0.1)  # Coffee break
    if address % 2 == 0:
        return "south"
    return "north"


def check(letter):
    random_number = random.random()
    if random_number < 0.5:
        return True
    return False


letters = [{"name": f"Person {i}", "address": i} for i in range(1, 10)]

# lets generate a bunch of letters


def process_letter(letter):
    if check(letter):
        print(f"Processing letter for {letter['name']} at {letter['address']}")
        direction = sort(letter["address"])
        print(f"Letter will be sent to the {direction} sub-office.")
    else:
        print(f"Impounding letter for {letter['name']} at {letter['address']}")


for letter in letters:
    process_letter(letter)
# No threading in this version, just sequential processing
