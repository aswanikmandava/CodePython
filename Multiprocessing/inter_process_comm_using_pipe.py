"""
Consider the program below, the function Pipe() returns two objects each representing one end of the pipe. 
The child process writes ten strings to the pipe which the parent prints on the console after retrieving them from the queue.
"""

from multiprocessing import Process, Pipe
import time

def sender(chn):
    for i in range(10):
        chn.send(f"Msg-{i}")
    # close the connection
    chn.close()


if __name__ == "__main__":
    parent_chn, child_chn = Pipe()
    p = Process(name="c_1", target=sender, args=(child_chn,))
    p.start()
    time.sleep(2)
    for _ in range(10):
        msg = parent_chn.recv()
        print(f"received {msg}")
    parent_chn.close()
    p.join()