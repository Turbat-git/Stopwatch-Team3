import asyncio
import time


start_time = time.time()
interval = time.time()

hour_time = 0
minute_time = 0
seconds_time = 0
micro_seconds = 0.0


async def timer():
    global micro_seconds
    global seconds_time
    global minute_time
    global hour_time
    global interval

    await asyncio.sleep(.1)

    micro_seconds += time.time() - interval
    interval = time.time()

    # count up to next time interval
    if micro_seconds >= 1:
        seconds_time += 1
        micro_seconds -= 1
    if seconds_time >= 60:
        minute_time += 1
        seconds_time -= 60
    if minute_time >= 60:
        hour_time += 1
        minute_time -= 60

    print(f"{hour_time}:{minute_time}:{seconds_time}")


while True:
    asyncio.run(timer())
