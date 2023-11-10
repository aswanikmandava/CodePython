from multiprocessing import Process, current_process
import os

def task():
    print(f"{current_process().name} has pid:{os.getpid()} with parent pid: {os.getppid()}")


if __name__ == "__main__":
    process_list = [0]*3
    print(f"Main process has name ({current_process().name}) with pid: {os.getpid()}")
    for i in range(3):
        # spawn a process to run task
        process_list[i] = Process(name=f"cp_{i}", target=task)
        process_list[i].start()
    
    for i in range(3):
        # wait for the child process to complete its task and join main thread
        process_list[i].join()
    