import multiprocessing as mp
colors = ['red', 'blue', 'green']

q = mp.Queue()

print(f"pushing items to queue")

for color in colors:
    q.put(color)

while(not q.empty()):
    # Queue.get(block=True, timeout=None)
    print(f"got {q.get()}")
    # Queue.get_no_wait() will never block, but will return Queue.Empty if the queue is empty.