"""
An example is presented below where two threads share a list and one of the threads tries to modify the list while the other attempts 
to read it. Using a lock object we make sure that the two threads share the list in a thread-safe manner.
"""
from threading import current_thread, Lock, Thread
import time

shared_list = [1, 2, 3]
list_lock = Lock()

def list_writer():
    this_thread = current_thread().getName()
    list_lock.acquire()
    print(f"{this_thread} has acquired the lock")
    time.sleep(3)
    shared_list[1] = 1000
    print(f"{this_thread} has modified the shared list. About to release the lock")
    list_lock.release()
    print(f"{this_thread} has released the lock")


def list_reader():
    this_thread = current_thread().getName()
    list_lock.acquire()
    print(f"{this_thread} has acquired the lock")
    print(f"{this_thread} has read the shared list value {shared_list[1]}")
    print(f"{this_thread} is about to release the lock")
    list_lock.release()
    print(f"{this_thread} has released the lock")


writer_thread = Thread(name="writer", target=list_writer, )
writer_thread.start()

reader_thread = Thread(name="reader", target=list_reader)
reader_thread.start()

writer_thread.join()
reader_thread.join()
