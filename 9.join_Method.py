# If a thread want to wait for any other thead then we use join method Ex. we want to upload a video on utube and send a notification to the subscribers the both task not run parallel

from threading import Thread
from time import sleep

def upload():
    print("Uploading starts.")
    sleep(3)
    print("Video Uploaded")
    
def notification():
    print("sending the notificatioon to subscribers")
    
t1=Thread(target=upload)
t2=Thread(target=notification)
t1.start()
t1.join()
t2.start()

for i in range(5):
    print("i love you rakhi")