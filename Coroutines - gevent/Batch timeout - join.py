import gevent
from gevent import Timeout
from time import time, sleep
from random import randint

def sleeper(t):
    secs = randint(5,10)
    print('%s -> preparing sleep for %s secs' % (t, secs))
    gevent.sleep(secs)
    

def test(m):
    print('>>> processing %s ...' % m)
    response = {}
    res = {}
    ip = {'m1': '1.2.3.4', 'm2': '2.3.4.5', 'm3':'3.4.5.6', 'm4':'5.6.6.7'}
    if m == 'm1':
        m1()
    elif m == 'm2':
        m2()
    elif m == 'm3':
        m3()
    elif m == 'm4':
        m4()
    res['status'] = 'Online'
    res['ip'] = ip[m]
    response[m] = res
    # f_resp.update(response)
    print('<<< processed %s ' % m)
    return response

def m1():
    print('m1 -> Inside')
    sleeper('m1')
    print('m1: doing some work')
    sleeper('m1')
    print('m1: doing some other work')
    print('m1: returning ...')

def m2():
    print('m2 -> Inside')
    sleeper('m1')
    print('m1: doing some task')
    print('m2: returning ...')

def m3():
    print('m3 -> Inside')
    sleeper('m3')
    print('m3: doing some stuff')
    sleeper('m3')
    print('m3: doing some other stuff')
    sleeper('m3')
    print('m3: doing final stuff')
    print('m3: returning ...')

def m4():
    print('m4 -> Inside')
    sleeper('m4')
    print('m4: doing some stuff')
    sleeper('m4')
    print('m4: doing some other stuff')
    sleeper('m4')
    print('m4: doing final stuff')
    print('m4: returning ...')

slrModemDetailsThreads = []
dataList = ['m1', 'm2', 'm3', 'm4']
finalResp = {}
response = {}
start = time()
modem_count = len(dataList)
GTHREAD_BATCH = 2
batch_counter = 0
batch = 0
BATCH_TIMEOUT = 6.0
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
        thread.join(timeout=BATCH_TIMEOUT)  # Set timeout for each job
        if thread.successful():
            finalResp.update(thread.value) # collect response
            print("SUCCESS for %s" % item)
        else:
            print("Something else for %s" % item)
            finalResp.update({item: 'timed_out'})  # Process result
            if thread.exception:
                print("Caught exception for %s" % item)
            else:
                print("Force stopping for %s" % item)
                thread.kill(block=False)

response.update({"modems":finalResp})
print("final resp: %s" % response)
finish = time()
print("Took %s sec" % (finish - start))
