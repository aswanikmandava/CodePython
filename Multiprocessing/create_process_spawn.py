from multiprocessing import Process, current_process
import multiprocessing
import os


class MyData:
    value = 10


def task():
    print(f"Process name ({current_process().name}), id {os.getpid()} value: ({MyData.value})")


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    # change the value of Test.value before creating
    # a new process
    MyData.value = 50
    p = Process(name='child_p', target=task)
    p.start()
    p.join()