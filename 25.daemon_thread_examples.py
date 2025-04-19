from threading import *
from time import sleep
def Display():
    for i in range(10):
        print("Teaching Section:",i)

t1=Thread(target=Display)
t1.daemon=True
t1.start()
sleep(0.2)
print("Exam time!")
print("Exam exam over!")
