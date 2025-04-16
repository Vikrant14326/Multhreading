#import thread class
from threading import Thread,current_thread
#create a function containg code to be execute parallaly

def display(n,msg):
    print("t1 thread details:",current_thread())
    for i in range(n):
        print(msg)
        
#create new threat hero
t1= Thread(target=display,kwargs={'n':3,'msg':"hellow"})

t1.start()

for i in range(5):
    print("new")