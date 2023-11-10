from multiprocessing import Process

def print_arg(continent="Asia"):
    print(f"Name of continent: {continent}")


if __name__ == "__main__":
    names = ['Europe', 'Australia', 'North America']
    # create a process with no arg
    proc_list = []
    proc = Process(target=print_arg)
    proc_list.append(proc)
    proc.start()

    # create processes with arg
    for name in names:
        proc = Process(target=print_arg, args=(name,))
        proc_list.append(proc)
        proc.start()

    # wait for process to finish
    for proc in proc_list:
        proc.join()

