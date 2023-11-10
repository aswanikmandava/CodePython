from multiprocessing import Pool
import os


def init(main_pid):
    print(f"Pool process with id ({os.getpid()}) received a process from main process ({main_pid})")

def square(num):
    return num*num

if __name__ == "__main__":
    main_pid = os.getpid()
    """
    processes is the number of worker processes to use. If processes is None then the number returned by os.cpu_count() is used, which is the number of CPUs on the system.
    initializer is an optional initialization method that is invoked before a process starts executing a task.
    initargs are the arguments passed to the initializer method.
    maxtasksperchild is the maximum number of tasks a pool process will execute before exiting. By default the pool process will live till the Pool exists.
    """
    proc_pool = Pool(processes=1, initializer=init, initargs=(main_pid,), maxtasksperchild=1)
    # submit a task to the pool process using apply method
    result = proc_pool.apply(square, args=(4,))
    print(result)
    