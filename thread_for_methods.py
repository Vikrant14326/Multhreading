from threading import Thread,current_thread

# class Example:
#     def display(self,n):
#         for i in range(n):
#             print("hellow world")

# e1=Example()
# t1=Thread(target=e1.display,args=(4,))
# t1.start()
###################################################
# class Example:
#     @classmethod
#     def display(self,n):
#         for i in range(n):
#             print("hellow world")

# e1=Example()
# t1=Thread(target=Example.display,args=(4,))
# t1.start()
###################################################
class Example:
    @staticmethod
    def display(n):
        for i in range(n):
            print("hellow world")

e1=Example()
t1=Thread(target=Example.display,args=(4,))
t1.start()
for i in range(7):
    print("hii")