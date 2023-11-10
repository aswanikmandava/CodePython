from threading import Thread, current_thread

class mythread(Thread):
    def __init__(self):
        Thread.__init__(self, 
                        name="my_subclass_thread",
                        args=(1, 2, 4),
                        )
    
    def run(self):
        this_thread = current_thread().getName()
        print(f"{this_thread} is executed")


t_obj = mythread()
t_obj.start()
t_obj.join()