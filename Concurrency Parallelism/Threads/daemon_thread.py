from threading import Thread, current_thread
import time


def task():
    while True:
        print(f"{current_thread().getName()} executing")
        time.sleep(1)


mythread = Thread(target=task, name="regular_thread", daemon=True)
mythread.start()

time.sleep(3)

print("Main thread is exiting ...")
