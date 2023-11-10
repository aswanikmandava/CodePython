"""
The above program is essentially a producer-consumer problem. The printer thread is a consumer and the finder thread is a producer. 
The printer thread needs to be signaled somehow that a prime number has been discovered for it to print.
Do you see a condition here? The condition in our program is the discovery of the prime number represented by the boolean variable found_prime.
Realize that locks don't help us signal other threads when a condition becomes true.

One shortcoming of the above code is we have the printer thread constantly polling in a while loop for the found_prime variable to become true.
This is called busy waiting and is highly discouraged as it unnecessarily wastes CPU cycles. Ideally, the printer thread should go to sleep so 
that it doesn't consume any system resources and be woken up when the condition it needs to act upon becomes true. This can be achieved 
through condition variables.
"""
from threading import Thread
import time


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:
        while not found_prime and not exit_prog:
            time.sleep(0.1)

        if not exit_prog:
            print(prime_holder)

            prime_holder = None
            found_prime = False


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True


def finder_thread_func():
    global prime_holder
    global found_prime

    i = 1

    while not exit_prog:

        while not is_prime(i):
            i += 1

        prime_holder = i
        found_prime = True

        while found_prime and not exit_prog:
            time.sleep(0.1)

        i += 1


found_prime = False
prime_holder = None
exit_prog = False

printer_thread = Thread(target=printer_thread_func)
printer_thread.start()

finder_thread = Thread(target=finder_thread_func)
finder_thread.start()

# Let the threads run for 5 seconds
time.sleep(3)

# Let the threads exit
exit_prog = True

printer_thread.join()
finder_thread.join()