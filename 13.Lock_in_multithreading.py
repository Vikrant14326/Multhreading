from threading import *
from time import sleep
My_Lock=Lock()

# def task(My_Lock,msg):
#     My_Lock.acquire()
#     for i in range(5):
#         print(msg)
#     sleep(3)
#     My_Lock.release()
# t1=Thread(target=task,args=(My_Lock,"hellow world"))      
# t2=Thread(target=task,args=(My_Lock,'welcome'))
# t1.start()    
# t2.start()  

##################################################################  
        
class Bus:
    def __init__(self,name,available_seats,l):
        self.l=l
        self.available_seats=available_seats
    def reserve(self,need_seats):
        self.l.acquire()
        print("Available seats are:",self.available_seats)
        if self.available_seats>=need_seats:
            nm=current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print(" Sorry! seats are not available")
        self.l.release()   
           

b1=Bus("Mahalakshami travels",3,My_Lock)
t1=Thread(target=b1.reserve,args=(1,),name="virat")       
t2=Thread(target=b1.reserve,args=(3,),name="nitin")       
t1.start()       
t2.start()   
    
