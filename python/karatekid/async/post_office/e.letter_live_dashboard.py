import asyncio
import random
import time
from collections import defaultdict

status_board = {}
transition_log = []
processing_times = {}
status_lock = asyncio.Lock()
sorter_limit = asyncio.Semaphore(10)


def timestamp():
    return time.strftime("%H:%M:%S")


def now():
    return time.time()


def determine_region(address):
    return {0: "Rural", 1: "Dublin", 2: "Midlands", 3: "West"}[address % 4]


async def log_transition(task_id, new_state):
    async with status_lock:
        status_board[task_id] = new_state
        transition_log.append((timestamp(), task_id, new_state))

        if new_state == "Queued":
            processing_times[task_id] = {
                "start": now(),
                "end": None,
                "direction": None,
                "region": None,
            }
        elif new_state.startswith("Delivered") or new_state.startswith("Handed off"):
            processing_times[task_id]["end"] = now()


async def sort(address, task_id):
    async with sorter_limit:
        region = determine_region(address)
        async with status_lock:
            processing_times[task_id]["region"] = region

        await log_transition(task_id, f"Sorting ({region})...")

        delay = {
            "Rural": random.uniform(5, 6),
            "Dublin": random.uniform(1, 2),
            "Midlands": random.uniform(2, 3),
            "West": random.uniform(3, 4),
        }[region]

        await asyncio.sleep(delay)
        return "south" if address % 2 == 0 else "north", region


def check(letter):
    return random.random() < 0.5


async def process_letter(letter, task_id):
    await log_transition(task_id, "Checking...")
    await asyncio.sleep(0.1)

    if check(letter):
        await log_transition(task_id, "Passed check. Routing to region...")
        direction, region = await sort(letter["address"], task_id)

        # Route rural differently
        if region == "Rural":
            await log_transition(task_id, "Handed off to rural carrier")
        else:
            await log_transition(task_id, f"Delivered to {direction}")
    else:
        await log_transition(task_id, "Impounded")


async def monitor_status():
    while True:
        await asyncio.sleep(5)
        async with status_lock:
            print(f"\n📋 Flight Board — {timestamp()}")
            for task_id, status in sorted(status_board.items()):
                print(f"  {task_id}: {status}")

            print("\n📊 Real-Time Status Summary:")
            state_counts = defaultdict(int)
            for status in status_board.values():
                key = status.split(".")[0]
                state_counts[key] += 1
            for state, count in sorted(state_counts.items()):
                print(f"  {state:<25}: {count}")
            print(f"  {'Total':<25}: {sum(state_counts.values())}")

            region_times = defaultdict(list)
            alerts = []
            for info in processing_times.values():
                if info["end"] is not None and info["region"]:
                    duration = info["end"] - info["start"]
                    region_times[info["region"]].append(duration)

            print("\n⏱ Region Summary:")
            for region in sorted(region_times):
                times = region_times[region]
                avg = sum(times) / len(times) if times else 0
                print(
                    f"  {region:<10}: {len(times)} letters, avg processing time: {avg:.2f}s"
                )

                # Alert if average processing time is high
                if avg > 4.5:
                    alerts.append(f"⚠️ ALERT: {region} region is slow (avg {avg:.2f}s)")

            if alerts:
                print("\n🚨 ALERTS:")
                for msg in alerts:
                    print(" ", msg)

            all_done = all(
                "Delivered" in s or "Handed off" in s or "Impounded" in s
                for s in status_board.values()
            )

        if all_done:
            break


async def main():
    letters = [{"name": f"Person {i}", "address": i} for i in range(1, 21)]
    monitor = asyncio.create_task(monitor_status())
    tasks = []

    for i, letter in enumerate(letters, start=1):
        task_id = f"Letter {i}"
        await log_transition(task_id, "Queued")
        task = asyncio.create_task(process_letter(letter, task_id))
        tasks.append(task)

    await asyncio.gather(*tasks)
    await monitor

    print("\n🗂️ Final Transition Log:")
    for entry in transition_log:
        print(f"{entry[0]}  |  {entry[1]}  →  {entry[2]}")


asyncio.run(main())
