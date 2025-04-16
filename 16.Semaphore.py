from threading import *
from time import sleep
obj=Semaphore(3)# default value is 1 work as RLoke or Lock 

def display(name):
    obj.acquire()
    for i in range(5):
        print("hellow")
        print(name)
        sleep(3)
    obj.release()
    obj.release()
    

t1= Thread(target=display,args=('Thread-1',))
t2= Thread(target=display,args=('Thread-2',))
t3= Thread(target=display,args=('Thread-3',))
t4= Thread(target=display,args=('Thread-4',))
t5= Thread(target=display,args=('Thread-5',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()