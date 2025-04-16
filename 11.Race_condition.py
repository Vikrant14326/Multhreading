from threading import Thread,current_thread


class Bus:
    def __init__(self,name,available_seats):
        self.available_seats=available_seats
    def reserve(self,need_seats):
        print("Available seats are:",self.available_seats)
        if self.available_seats>=need_seats:
            nm=current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("seats are not available")    

b1=Bus("Mahalakshami travels",2)
t1=Thread(target=b1.reserve,args=(1,),name="virat")       
t2=Thread(target=b1.reserve,args=(1,),name="nitin")       
t1.start()       
t2.start()       
    