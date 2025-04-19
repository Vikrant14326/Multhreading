import threading 

def task():
    for i in range(5):
        print("hello")
        
timer=threading.Timer(10,task)

timer.start()

for i in  range(5):
    print("Main thread")  