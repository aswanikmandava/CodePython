from multiprocessing import Process, current_process, Queue
import os
import multiprocessing
import random
import sys

def consumer(q):
    count = 0
    pname = current_process().name
    while (not q.empty()):
        # get() is a blocking call
        # print(f"{pname} Got {q.get()}")
        # you can unblock it this way
        try:
            msg = q.get(block=False, timeout=3)
            print(f"{pname} Got {msg}")
            count += 1
        except Exception:
            pass
    print(f"Process ({pname}) with id ({os.getpid()}) consumed {count} items")

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    data_q = Queue()
    random.seed()
    for _ in range(100):
        data_q.put(random.randrange(10))
    # spawn 2 child processes to consume data
    p1 = Process(name="child_1", target=consumer, args=(data_q,))
    p2 = Process(name="child_2", target=consumer, args=(data_q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()