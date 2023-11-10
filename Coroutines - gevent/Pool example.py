from multiprocessing import pool
from random import randrange
from time import sleep, time
import gevent
from gevent.pool import Pool

GTHREAD_BATCH = 4
g_pool = Pool(GTHREAD_BATCH) # Run these many greenlets at once
def call_eta_service(driver):
    # simulates network call to ETA service
    print(f"==> starting eta computation for: {driver}")
    sleep(5)
    print(f"<== ending eta computation for: {driver}")

passengers = ['shiv', 'roy', 'aswani', 'kumar', 'mandava', 'suneetha', 'bodavula', 'anil']
pass_count = len(passengers)

start = time()
count = 0
for pasn in passengers:
    count += 1
    if count % GTHREAD_BATCH == 0:
        print(f"Batch ID - {count}")
    g_pool.spawn(call_eta_service, pasn) # blocks control when the pool size equals GTHREAD_BATCH
g_pool.join() # blocks control until the previous pool is completed
finish = time()
print(f"Took {finish - start}s")