import threading
import time

number_of_players=4
barrier=threading.Barrier(number_of_players)
def player(name):
    print(f"{name} started")
    score=0
    for i in range(5):
        time.sleep(3)
        print(f"{name} is playing")
        
    barrier.wait()
    
    
    print(f"{name} scored {score}")
    
    print(f"sending winning amount to {name}")

players_name=['virat','rakhi','nitin','plk']
Threads=[]
for name in players_name:
    thread=threading.Thread(target=player,args=(name,))
    Threads.append(thread)
    thread.start()
    

    
    

        
    