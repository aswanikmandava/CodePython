arr = ['one', 'two', 3, 1, 2, 4, 5, 6]
count = len(arr)
bsize = 2
batches = []

batch = 0
for i in range(0, count, bsize):

    # print(f"iterator - {i} batch - {batch}")
    batches.append(arr[i:i+bsize])
    # print(f"batch - {batch}")
    batch += 1

print(f"final - {batches}")