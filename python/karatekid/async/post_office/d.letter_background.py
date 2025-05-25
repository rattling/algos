import asyncio
import random

# Shared stats
stats = {"processed": 0, "impounded": 0, "north": 0, "south": 0}
stats_lock = asyncio.Lock()
sorter_limit = asyncio.Semaphore(10)


def check(letter):
    return random.random() < 0.5


async def sort(address):
    async with sorter_limit:
        if random.random() < 0.5:
            await asyncio.sleep(1)
        return "south" if address % 2 == 0 else "north"


async def process_letter(letter):
    if check(letter):
        print(f"Processing letter for {letter['name']} at {letter['address']}")
        direction = await sort(letter["address"])
        async with stats_lock:
            stats["processed"] += 1
            stats[direction] += 1
        print(f"Letter sent to the {direction} sub-office.")
    else:
        print(f"Impounding letter for {letter['name']} at {letter['address']}")
        async with stats_lock:
            stats["impounded"] += 1


async def letter_stream():
    """Simulates a stream of incoming letters every 0.1s"""
    for i in range(1, 101):
        letter = {"name": f"Person {i}", "address": i}
        yield letter
        await asyncio.sleep(0.1)


async def main():
    tasks = []
    async for letter in letter_stream():
        task = asyncio.create_task(process_letter(letter))
        tasks.append(task)

        # Optional: clean up completed tasks
        tasks = [t for t in tasks if not t.done()]

        # Optional: print how many still running
        print(f"📦 Active background tasks: {len(tasks)}")

    # Wait for remaining tasks to finish
    if tasks:
        print("⌛ Waiting for background tasks to complete...")
        await asyncio.gather(*tasks)

    # Final stats
    print("\n📬 Final Stats:")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")


asyncio.run(main())
