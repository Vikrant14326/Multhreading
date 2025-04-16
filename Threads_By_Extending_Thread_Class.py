from time import sleep
from threading import Thread
videos= ['OOP Sylabous','constractor','destractor','file handling']

class MyClass(Thread):
    def __init__(self,val):
        print("constractor called")
        self.kid=val
        Thread.__init__(self)
    def compration(self):
        print("compration code is here")      
    def run(self):
        a=10
        b=40
        self.compration()
        if self.kid:
            print("Sutable for kid")
        for vid in videos:
            print(f"{vid} start uploading...")
            sleep(3)
            print(f"{vid} uploading.")
        self.temp=a+b

t1=MyClass(False)
t1.start()
sleep(15)
print("result is:",t1.temp)

for i in range(4):
    sleep(0.5)
    print("checking copyrights")