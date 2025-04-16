from threading import Thread,current_thread
import os
def display():
    for i in range(4):
        print("hellow world")
        
def show():
    for i in range(3):
        print("welcome")

t1=Thread(target=display)
t2=Thread(target=show)
print(t1.name)
print(t2.name)
# print(t1.getName())
# print(t2.getName())

# How to change the name of existing thread
t1.name="vikrant"
print(t1.name)
#how to change the name of main thread
current_thread().name="rakhi"
print("main thread name:",current_thread().name)

########################################################## IDENTIFIER ####################################

#    (1)   Threading Identifier----> gives through process
#        i.each thread have unique identifier(id) within the python proces
#        (ii) Assigned  by python interprater
#        (iii) read only pisitive integer and unique in nature
#         assign after start the thread
#    (2)   Native Identifier-------> gives through OS
#         i.each thread have unique identifier(id) 
#         property name is native_id(assign after start the thread)
#        genraly ident and native_id are the same

###########################################################################################################
t1.start()
t2.start()
print(t1.ident)
print(t1.native_id)
print(os.getpid())