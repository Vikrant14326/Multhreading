from threading import *
import threading
from time import sleep

def custome_hooks(args):
    print("Exaption occured in thread")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def display():
    for i in range(5):
        sleep(3)
        print("hellow:"+10)
        
def show():
    for i in range(4):
        print("hellow")
        sleep(0.5)
threading.excepthook=custome_hooks
t1=Thread(target=display)
t2=Thread(target=show)
t1.start()        
t2.start()
t1.join()
t2.join()

for i in range(4):
    print("By")        