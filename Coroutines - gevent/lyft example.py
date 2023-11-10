from random import randrange
from time import sleep, time
from dataclass_example import *
import gevent

def call_eta_service(user, driver) -> ETA:
    # simulates network call to ETA service
    print(f"starting eta computation for: {driver.name}")
    sleep(0.5)
    print(f"ending eta computation for: {driver.name}")
    return ETA(user, driver, randrange(60))

def match(user, drivers) -> Driver:
    etas = [
        call_eta_service(user, driver)
        for driver in drivers
    ]
    return min(etas, key=lambda eta: eta.seconds).driver

drivers = [Driver('shiv'), Driver('roy')]
passengers = [Passenger('alice'), Passenger('bob')]

start = time()
# [match(pasn, drivers) for pasn in passengers]
gevent.joinall([gevent.spawn(match, pasn, drivers) for pasn in passengers])
finish = time()
print(f"Took {finish - start}s")