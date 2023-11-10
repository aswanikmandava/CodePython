from multiprocessing import Process, current_process
import os


def task(name, count=0):
    print(f"Spawned task {name} (pid: {os.getpid()}) with input {count}")


if __name__ == "__main__":
    p = Process(name="myprocess", target=task, args=('child_p',), kwargs={'count': 5})
    p.start()
    p.join()