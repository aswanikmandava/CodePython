import gevent
from gevent import Timeout
from time import time, sleep

def test(m):
    print('>>> processing %s ...' % m)
    response = {}
    res = {}
    ip = {'m1': '1.2.3.4', 'm2': '2.3.4.5', 'm3':'3.4.5.6'}
    if m in ['m1', 'm2']:
        #sleep(10.0)
        gevent.sleep(10)
    else:
        #sleep(0.5)
        gevent.sleep(0.5)
    res['status'] = 'Online'
    res['ip'] = ip[m]
    response[m] = res
    # f_resp.update(response)
    print('<<< processed %s ' % m)
    return response

slrModemDetailsThreads = []
dataList = ['m1', 'm2', 'm3']
finalResp = {}
response = {}
start = time()
modem_count = len(dataList)
GTHREAD_BATCH = 3
batch_counter = 0
batch = 0
BATCH_TIMEOUT = 3.0
for i in range(0, modem_count, GTHREAD_BATCH):
    batch += 1
    batch_mem = dataList[i:i+GTHREAD_BATCH]
    print("processing batch - %s" % batch)
    batch_threads = []
    thread_map = {}
    # Spawn greenlets for each batch
    for m in batch_mem:
        thread = gevent.spawn(test, m)
        batch_threads.append(thread)
        thread_map[thread] = m
    for thread in batch_threads:
        item = thread_map[thread]
        result = None
        thread.join(timeout=BATCH_TIMEOUT)  # Set timeout for each job
        try:
            result = thread.get(block=False)    # collect response
            finalResp.update(result)
            print("SUCCESS for %s" % item)
        except (Timeout, Exception):
            print("Caught exception for %s" % item)
            finalResp.update({item: 'timed_out'})  # Process result
            
    # completed = gevent.joinall(batch_threads, timeout=BATCH_TIMEOUT)
    # completed = gevent.joinall(batch_threads)
    # [finalResp.update(thread.value) if thread.value else finalResp.update({thread_map[thread]: 'timed_out'}) for thread in batch_threads]

response.update({"modems":finalResp})
print("final resp: %s" % response)
finish = time()
print("Took %s sec" % (finish - start))
