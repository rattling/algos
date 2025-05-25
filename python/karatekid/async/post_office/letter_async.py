import asyncio
import random

# Tracking stats
stats = {"processed": 0, "impounded": 0, "north": 0, "south": 0}
stats_lock = asyncio.Lock()


async def sort(address):
    if random.random() < 0.5:
        await asyncio.sleep(1)  # Simulate delay (coffee break)
    return "south" if address % 2 == 0 else "north"


async def check(letter):
    return random.random() < 0.5


async def process_letter(letter):
    if await check(letter):
        print(f"Processing letter for {letter['name']} at {letter['address']}")
        direction = await sort(letter["address"])
        async with stats_lock:
            stats["processed"] += 1
            stats[direction] += 1
        print(f"Letter will be sent to the {direction} sub-office.")
    else:
        print(f"Impounding letter for {letter['name']} at {letter['address']}")
        async with stats_lock:
            stats["impounded"] += 1


async def main():
    letters = [{"name": f"Person {i}", "address": i} for i in range(1, 101)]

    # Launch all processing tasks concurrently
    tasks = [process_letter(letter) for letter in letters]
    await asyncio.gather(*tasks)

    # Show final results
    print("\n📬 Final Stats:")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")


# Run the event loop
asyncio.run(main())
