from concurrent.futures import ProcessPoolExecutor, as_completed
import time

if __name__ == '__main__':
    s_time = time.time()
    pow_list = [i for i in range(5)]
    print(f"starting ...{pow_list}")
    with ProcessPoolExecutor() as executor:
        t_futures = [executor.submit(pow, i, i) for i in pow_list]
    """
    In order to allow our program to continue running, we get back these futures that represent a placeholder for a value. 
    If we try to print the future, depending on whether it's finished running or not, we'll either get back a state of 
    "pending" or "finished." Once it's finished we can get the return value (assuming there is one) using var.result(). 
    In this case, our var will be "result."
    """
    for f in as_completed(t_futures):
        print(f"future {f} result: {f.result()}")
    e_time = time.time()
    print(f"Execution took {(e_time - s_time)} secs")