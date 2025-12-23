import threading 


counter = 0

# ----------- without lock ----------------------

def without_lock(): 
    global counter 
    for _ in range(100000):
        counter += 1

threads=[threading.Thread(target=without_lock) for _ in range(3)]

for t in threads : t.start()
for t in threads : t.join()
print("Final counter without lock:", counter)  # Likely incorrect


# ----------------With Lock ----------------------

def with_lock():
    global counter 
    for _ in range(100000):
        with threading.Lock():
            counter += 1

threads=[threading.Thread(target=with_lock) for _ in range(3)]
for t in threads : t.start()
for t in threads : t.join()
print("Final counter with lock:", counter)  # Should be correct