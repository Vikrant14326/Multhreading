from threading import Thread
import time

def square(num):
    print("finding square..")
    time.sleep(1)
    print(f"square of {num} is:",num**2)

def cube(num):
    print("finding cube...")
    time.sleep(1)
    print(f"cube of {num} is:",num**3)
 
begin= time.time()
# square(3)
# cube(3) 
# print("total time taken:",time.time()-begin) 

t1=Thread(target=square,args=(2,))
t2=Thread(target=cube,args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print("total time taken:",time.time()-begin)
