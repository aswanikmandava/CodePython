from multiprocessing import pool
from random import randrange
from time import sleep, time
import gevent

GTHREAD_BATCH = 4
def call_eta_service(driver):
    # simulates network call to ETA service
    print(f"==> starting eta computation for: {driver}")
    # sleep(2)
    gevent.sleep(2)
    print(f"<== ending eta computation for: {driver}")

passengers = ['shiv', 'roy', 'aswani', 'kumar', 'mandava', 'suneetha', 'bodavula', 'anil']
pass_count = len(passengers)

start = time()
count = 0
for i in range(0, pass_count, GTHREAD_BATCH):
    batch_mem = passengers[i:i+GTHREAD_BATCH]
    print(f"batch => {batch_mem}")
    # process each batch async
    gevent.joinall([gevent.spawn(call_eta_service, pasn) for pasn in batch_mem])
finish = time()
print(f"Took {finish - start}s")

"""
OUTPUT (when blocking code is in use - sleep)
-------------------------------------------------
batch => ['shiv', 'roy', 'aswani', 'kumar']
==> starting eta computation for: shiv
<== ending eta computation for: shiv
==> starting eta computation for: roy
<== ending eta computation for: roy
==> starting eta computation for: aswani
<== ending eta computation for: aswani
==> starting eta computation for: kumar
<== ending eta computation for: kumar
batch => ['mandava', 'suneetha', 'bodavula', 'anil']
==> starting eta computation for: mandava
<== ending eta computation for: mandava
==> starting eta computation for: suneetha
<== ending eta computation for: suneetha
==> starting eta computation for: bodavula
<== ending eta computation for: bodavula
==> starting eta computation for: anil
<== ending eta computation for: anil
Took 16.11890721321106s
"""

"""
OUTPUT (when unblocking code is in use - gevent.sleep)
-------------------------------------------------------
batch => ['shiv', 'roy', 'aswani', 'kumar']
==> starting eta computation for: shiv
==> starting eta computation for: roy
==> starting eta computation for: aswani
==> starting eta computation for: kumar
<== ending eta computation for: shiv
<== ending eta computation for: roy
<== ending eta computation for: aswani
<== ending eta computation for: kumar
batch => ['mandava', 'suneetha', 'bodavula', 'anil']
==> starting eta computation for: mandava
==> starting eta computation for: suneetha
==> starting eta computation for: bodavula
==> starting eta computation for: anil
<== ending eta computation for: mandava
<== ending eta computation for: suneetha
<== ending eta computation for: bodavula
<== ending eta computation for: anil
Took 4.044698715209961s
"""