import gevent
from gevent import Timeout
import time
SLEEP = 6
TIMEOUT = 5
timeout = Timeout(TIMEOUT)
timeout.start()
 
def wait():
    gevent.sleep(SLEEP)
    print('log in wait')
begin = time.time()
try:
    gevent.spawn(wait).join()
except Timeout:
    print('after %s catch Timeout Exception' % (time.time() - begin))
finally:    
    timeout.cancel()