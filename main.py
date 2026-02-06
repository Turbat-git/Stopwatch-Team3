import asyncio
import time

stop_time = 0.0
start_time = time.time()


async def timer(stop_time: float):
    stop_time += 0.1
    await asyncio.sleep(.1)
    print(f"{round(time.time() - start_time)}")
    return stop_time

while True:
    stop_time = asyncio.run(timer(stop_time))
