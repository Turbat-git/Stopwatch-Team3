import asyncio
import time

# stop_time = 0.0
start_time = time.time()


async def timer():
    # stop_time += 0.1
    await asyncio.sleep(.1)
    print(f"{round(time.time() - start_time)}")

while True:
    asyncio.run(timer())
