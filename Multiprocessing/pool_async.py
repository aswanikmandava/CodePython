from multiprocessing import Pool
import os
import time


def init(main_pid):
    print(f"Pool process with id ({os.getpid()}) received a process from main process ({main_pid})")

def square(num):
    return num*num

def on_success(result):
    # success callback
    print(f"task success with result: {result}")

def error_cb(err):
    # error callback
    print(f"task failed with error: {err}")

if __name__ == "__main__":
    main_pid = os.getpid()
    """
    processes is the number of worker processes to use. If processes is None then the number returned by os.cpu_count() is used, which is the number of CPUs on the system.
    initializer is an optional initialization method that is invoked before a process starts executing a task.
    initargs are the arguments passed to the initializer method.
    maxtasksperchild is the maximum number of tasks a pool process will execute before exiting. By default the pool process will live till the Pool exists.
    """
    proc_pool = Pool(processes=1, initializer=init, initargs=(main_pid,), maxtasksperchild=2)
    # submit a task to the pool process using apply method
    result = proc_pool.apply_async(square, args=(4,), callback=on_success, error_callback=error_cb)
    # prevent main from exiting before the pool process completes
    time.sleep(6)