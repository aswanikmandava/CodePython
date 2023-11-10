import dis

count = 0

def increment(count):
    count += 1

print(dis.dis(increment))