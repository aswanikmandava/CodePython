from operator import ge
from socket import timeout
import gevent
from gevent import Greenlet, Timeout
from time import time, sleep

def test(m, f_resp):
    print('>>> processing %s ...' % m)
    response = {}
    res = {}
    ip = {'m1': '1.2.3.4', 'm2': '2.3.4.5', 'm3':'3.4.5.6'}
    if m != 'm1':
        gevent.sleep(6)
    else:
        gevent.sleep(0.5)
    # if m == 'm3':
    #     res2 = 30/0
    res['status'] = 'Online'
    res['ip'] = ip[m]
    response[m] = res
    f_resp.update(response)
    print('<<< processed %s ' % m)
    return response

def handle_except(g_obj):
    try:
        result = g_obj.get(block=True, timeout=BATCH_TIMEOUT)
        print("Captured result - %s" % result)
    except Timeout:
        print("modem timedout")
    except Exception as e:
        print("Caught greenlet exception: %s" % e)

def handle_exception(g_obj):
    try:
        if g_obj.value:
            print("Captured result - %s" % g_obj.value)
        elif g_obj.exception:
            print("Caught greenlet exception: %s" % g_obj.exception)
    except Exception as e:
        print("Caught greenlet exception: %s" % e)

slrModemDetailsThreads = []
dataList = ['m1', 'm2', 'm3']
finalResp = {}
response = {}
start = time()
modem_count = len(dataList)
GTHREAD_BATCH = 2
batch_counter = 0
batch = 0
BATCH_TIMEOUT = 3.0
for i in range(0, modem_count, GTHREAD_BATCH):
    batch += 1
    batch_mem = dataList[i:i+GTHREAD_BATCH]
    print("processing batch - %s" % batch)
    batch_threads = [gevent.spawn(test, m, finalResp) for m in batch_mem]
    # process each batch async
    # try:
    # wait for 3 secs to allow the greenlets to finish
    completed = gevent.joinall(batch_threads)
    print("completed %s threads in this batch of size (%s)" % (len(completed), len(batch_threads)))
    [handle_except(thread) for thread in batch_threads]
        # for thread in batch_threads:
        #     if thread.value:
        #         print("thread is processed. result: %s" % thread.value)
        #     if thread.exception:
        #         print("caught thread exception %s" % thread.exception)
    # except Timeout:
    #     print("Batch %s timedout" % batch)

"""
for item in dataList:
    modem_count -= 1
    print(f"batch_counter: {batch_counter}, modem_count = {modem_count}")
    if item != '':
        print(f"processing {item}")
    if batch_counter < GTHREAD_BATCH:
        slrThread = Greenlet.spawn(test, item, finalResp)
        slrModemDetailsThreads.append(slrThread)
        batch_counter += 1
        print(f"spawned greenlet - {batch_counter}")
    if (batch_counter == GTHREAD_BATCH or modem_count == 0):
        print(f"spawned a greenlet batch - {batch_counter}")
        for thread in slrModemDetailsThreads:
            rresult = thread.get(block=True, timeout=2.0)  # get the response
            print("greenlet response - %s" % rresult)
            finalResp.update(rresult)
            print("waiting for threads to complete ...")
            gevent.joinall(slrModemDetailsThreads)
            print("all batch threads completed ...")
            batch_counter = 0   # reset counter
            slrModemDetailsThreads = [] # re-init array
"""
response.update({"modems":finalResp})
print("final resp: %s" % response)
finish = time()
print("Took %s sec" % (finish - start))
