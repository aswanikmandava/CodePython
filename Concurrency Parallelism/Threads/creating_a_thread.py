from threading import Thread, current_thread


def task(a, b, c, **kwargs):
    cur_thread = current_thread().getName()
    print(f"{cur_thread} received args - {a}, {b}, {c}, {kwargs}")


mythread = Thread(  group=None, # reserved
                    target=task, # callable object
                    name="demo thread", # name of thread
                    args=(1, 2, 3), # args passed to the target
                    kwargs={
                      "fname": "Aswani",
                      "lname": "Mandava"}, # dictionary of keywords arguments
                    daemon=None # set True to make the thread a daemon
                  )

mythread.start()    # start the thread

mythread.join()     # wait for the thread to finish