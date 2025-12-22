import threading
import time

def task(name):
    """A function simulating an I/O-bound task."""
    print(f"Thread {name}: starting...")
    time.sleep(2) # Simulate an I/O operation
    print(f"Thread {name}: finishing.")

# Create threads
thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))

# Start the threads
thread1.start()
thread2.start()

print("Main thread: doing other work concurrently.")

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Main thread: all done.")
