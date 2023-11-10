from threading import Thread, RLock
"""
A reentrant lock is defined as a lock which can be reacquired by the same thread. A RLock object carries the notion of ownership. 
If a thread acquires a RLock object, it can chose to reacquire it as many times as possible.
Note that it is imperative to release the lock as many times as it is locked, otherwise the lock remains in locked state and 
any other threads attempting to acquire the lock get blocked. 
"""

def child_task():
    r_lock.acquire()
    print("task is executing")
    r_lock.release()

r_lock = RLock()
r_lock.acquire()
r_lock.acquire()
r_lock.release()

# uncomment below line for program to exit normally
# r_lock.release()

worker = Thread(name="w_thread", target=child_task)
worker.start()
worker.join()