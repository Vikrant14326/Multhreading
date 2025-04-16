from threading import Thread,current_thread,main_thread,active_count,enumerate,get_native_id
import os
def display():
    print("details of main thread:",main_thread())
    print("native id of t1:",get_native_id())
    for i in range(4):
        print("hellow world")
        
def show():
    for i in range(3):
        print("welcome")

t1=Thread(target=display)
t2=Thread(target=show)
print("Before:",t1.is_alive())
t1.start()
print("After:",t1.is_alive())
print("native id of main thread:",get_native_id())


print("number of threads:",enumerate())
print("number of threads:",active_count())
