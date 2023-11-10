Greenlets are scheduled immediately when you call greenlet.spawn().

gevent.joinall() doesn't execute greenlets - it only tells the main thread (the one that actually spawned them) to wait for the ones passed in as parameters to finish running. 
Not calling joinall runs the risk of the main thread finishing and exiting before the results of the greenlets in joinall() has been reached, and then who's going to handle their results?

gevent.sleep doesn't block the main thread

killall(block=True, timeout=3.0)
timeout parameter is is only honored when block is True

REF:
http://ftp.esrf.eu/pub/bliss/gevent_guijarro_sglab.html#slide30