# Traffic Signal Simulation
import threading
from time import sleep

e = threading.Event()

def light_switch():
    while True:
        print("Light is GREEN")
        e.set()  # Allow traffic to go
        sleep(5)

        print("Light is RED")
        e.clear()  # Stop the traffic
        sleep(5)

def traffic_message():
    while True:
        if e.is_set():
            print("You can go!")
        else:
            print("Please stop...")
        sleep(0.5)

t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()
