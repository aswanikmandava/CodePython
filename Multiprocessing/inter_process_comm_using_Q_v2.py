"""
The problem with v1 snippet is that a process can find the q.empty() to be false but before it gets a chance to take the 
last item off the queue, another process may have already removed it. Thus, our process ends up getting blocked on the 
get call because the queue is empty.

Using locks can we avoid the described situation? The key is to make the emptiness check and the get call atomic, i.e. 
when a process executes the two calls, no other process should be able to make the same calls.
"""
from multiprocessing import Process, current_process, Queue, Lock
import os
import multiprocessing
import random
import sys
import time

def consumer(q, q_lock):
    count = 0
    pname = current_process().name
    keep_going = True
    while keep_going:
        q_lock.acquire()
        if not q.empty():
            q.get()
            count += 1
        else:
            keep_going = False
        q_lock.release()
        # Added this sleep so that not all items get processed by
        # a single process
        time.sleep(0.001)
    print(f"Process ({pname}) with id ({os.getpid()}) consumed {count} items")

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    data_q = Queue()
    q_lock = Lock()
    random.seed()
    for _ in range(100):
        data_q.put(random.randrange(10))
    # spawn 2 child processes to consume data
    p1 = Process(name="child_1", target=consumer, args=(data_q, q_lock))
    p2 = Process(name="child_2", target=consumer, args=(data_q, q_lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()