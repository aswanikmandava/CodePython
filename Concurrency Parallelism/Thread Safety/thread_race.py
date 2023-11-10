from threading import *
import random
import time

rand_int = 0


def updater():
    global rand_int
    while 1:
        rand_int = random.randint(1, 9)
        # print(f"Updated: {rand_int}")


def printer():
    global rand_int
    while 1:

        # test
        if rand_int % 5 == 0:
            print(f"Checked value: {rand_int}")
            if rand_int % 5 != 0:   # rand_int is modified by the modifier thread
                # and act
                print(f"Stale value: {rand_int}")


if __name__ == "__main__":
    Thread(target=updater, daemon=True).start()
    Thread(target=printer, daemon=True).start()

    # Let the simulation run for 2 seconds
    time.sleep(2)