# cheking daemon nature of main thread

from threading import *
obj=current_thread()
print("Nature of main thread:",obj.daemon)

#How to change daemon nature of thread

def Display():
    print("This is displat function")
    
t1=Thread(target=Display)
print("Nature of t1 thread:",t1.daemon)
t1.daemon=True # Also can use t1.setDaemon(True)
# t1.setDaemon(True)
print("Nature of t1 thread after change:",t1.daemon)

t1.start()
