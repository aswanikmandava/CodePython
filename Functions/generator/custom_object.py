class MyIterator:
    def __init__(self, start, end) -> None:
        self.num = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num


obj = MyIterator(start=1, end=6)
# get an iterator object
i_obj = iter(obj)

while True:
    try:
        print(next(i_obj))
    except Exception as e:
        print(f"ERR: {e}")
        break