"""
The task is to compute the sum of all the integers from 0 to 3000000 (3 million). 
In the first scenario, we have a single thread doing the summation while in the second scenario, 
we split the range into two parts and have one thread sum for each range. Once both the threads are complete, 
we add the two half sums to get the combined sum. 
Finally, we repeat the previous exercise using processes instead of threads. 
We measure the time taken for each scenario and print it.
"""
from multiprocessing import Process
from threading import Thread
from multiprocessing.managers import BaseManager
import time
import multiprocessing

class SumUp:
    def __init__(self) -> None:
        self.total = 0

    def sum_integers(self, start, end):
        for i in range(start, end + 1):
            self.total += i

    def get_sum(self):
        return self.total

def sum_single_thread():
    stime = time.time()
    obj = SumUp()
    obj.sum_integers(1, 3000000)
    total_sum = obj.get_sum()
    etime = time.time()
    duration = etime - stime
    print(f"Sum by single thread ({total_sum}) took {duration} secs")

def sum_by_2_threads():
    obj1 = SumUp()
    obj2 = SumUp()
    stime = time.time()
    t1 = Thread(target=obj1.sum_integers, args=(1, 1500000))
    t2 = Thread(target=obj2.sum_integers, args=(1500001, 3000000))
    t1.start()
    t2.start()
    t1.join(timeout=10)
    t2.join(timeout=10)
    combined_total = obj1.get_sum() + obj2.get_sum()
    etime = time.time()
    duration = etime - stime
    print(f"Sum by 2 threads ({combined_total}) took {duration} secs")

def single_process(obj1, start, end):
    obj1.sum_integers(start, end)

def sum_by_2_processes():
    BaseManager.register('SumUp', SumUp)
    mgr = BaseManager(address=('127.0.0.1', 63333))
    mgr.start()
    obj1 = mgr.SumUp()
    obj2 = mgr.SumUp()
    stime = time.time()
    p1 = Process(target=single_process, args=(obj1, 1, 1500000))
    p2 = Process(target=single_process, args=(obj2, 1500001, 3000000))
    p1.start()
    p2.start()
    p1.join(timeout=10)
    p2.join(timeout=10)
    combined_total = obj1.get_sum() + obj2.get_sum()
    etime = time.time()
    duration = etime - stime
    print(f"Sum by 2 processes ({combined_total}) took {duration} secs")

if __name__ == '__main__':
    print(f"system has {0} cpus".format(multiprocessing.cpu_count()))
    sum_single_thread()
    sum_by_2_threads()
    sum_by_2_processes()