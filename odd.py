import threading
from time import sleep
def workodd():
    x=1
    while 1:
        x=x+2
        print x
        sleep(0.5)
def workeven():
    x=0
    while 1:
        x=x+2
        print x
        sleep(0.5)
t1=threading.Thread(target=workodd)
t2=threading.Thread(target=workeven)
t1.start()
t2.start()


