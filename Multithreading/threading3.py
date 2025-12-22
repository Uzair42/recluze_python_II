import threading 
import time 

def walking():
    time.sleep(8)
    print(" Walking is done ")

def running():
    time.sleep(5)
    print(" Running is done ")

def swimming():
    time.sleep(3)
    print(" Swimming is done ") 


#---------- In sequential it will take 8+5+3=16 seconds -------------
# walking()
# running()
# swimming()
# print(" All activities are done ")
#--------------------------------------------------------------------

#---------- In multithreading it will take max(8,5,3)=8 seconds -------------

t1=threading.Thread(target=walking  )
t2=threading.Thread(target=running  )
t3=threading.Thread(target=swimming  )

t1.start()
t2.start()
t3.start()

#---------------------------------------------------------------------------


t1.join()
t2.join()
t3.join()
#-------------main thread work ----------------
print(" Main thread is doing other work ")
