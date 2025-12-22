import threading 
import requests 
import time



def gist():
  # for i in range(100):

    
    print(" Sleep")
    time.sleep(5)

    # print(i )


thread=[]

for i in range(5):
 t=threading.Thread(target=gist)
 print("threading.Thread(target=()) ")
 t.start()
 print(f"Thread : {i}")
 print(f"Thread info : {t.getName} \n")

 thread.append(t) 

for i in thread:
  t.join()



