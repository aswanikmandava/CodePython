"""
Every data structure, open file, and database connection that exists in the parent process is copied over, 
open and ready to use, in the child process. Consider the below program, we open a file for writing in the 
parent process and then subsequently write to it from the child process. The file descriptor is a global variable,
a copy of which is also received by the child process. This demonstrates that the child process is an identical copy of 
the parent process.

NOTE: The fork method can't be used on a Windows platform.
"""
from multiprocessing import Process, current_process
import multiprocessing
import os

fh = None

def task():
    fh.write(f"Log written by {current_process().name} with pid {os.getpid()}")
    fh.flush()


if __name__ == "__main__":
    multiprocessing.set_start_method('fork')
    fh = open("tmp.txt", "w")
    fh.write(f"Log written by {current_process().name} with pid {os.getpid()}")
    p = Process(name='child', target=task)
    p.start()
    p.join()
    fh.close()

    # print the file contents
    with open("tmp.txt", "r") as file_d:
        print(file_d.readlines())
    # remove file
    os.remove("tmp.txt")