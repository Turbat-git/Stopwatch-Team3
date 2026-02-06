import asyncio
import time

'''
lap function: show lap number and time
https://www.geeksforgeeks.org/python/python-program-to-create-a-lap-timer/
'''

start_time = time.time()


def lap_time():
    lap_num = 1
    last_lap = start_time
    try:
        while True:
             # press enter to make a lap
            input()

            lap_time = round((time.time() - last_lap), 2)

            print(f"lap number: {lap_num} ")
            print(f"lap time: {lap_time}")

            last_lap = time.time()
            lap_num += 1

    except KeyboardInterrupt:
        print("Done")



if __name__ == '__main__':
    while True:
        lap_time()