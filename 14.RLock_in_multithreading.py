from threading import *
from time import sleep
My_Lock=RLock()

class Bus:
    def __init__(self,name,available_seats,l):
        self.l=l
        self.available_seats=available_seats
    def reserve(self,need_seats):
        self.l.acquire()
        self.l.acquire()
        print("Available seats are:",self.available_seats)
        if self.available_seats>=need_seats:
            nm=current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print(" Sorry! seats are not available")
        self.l.release()   
        self.l.release()   
           

b1=Bus("Mahalakshami travels",3,My_Lock)
t1=Thread(target=b1.reserve,args=(1,),name="virat")       
t2=Thread(target=b1.reserve,args=(3,),name="nitin")       
t1.start()       
t2.start()   