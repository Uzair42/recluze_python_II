

### Sequential approch  and parallel approch 
```python

import threading
import requests
import time
```
Define function for having real time taking tasks
```python
urls = ["https://google.com", "https://python.org", "https://github.com"] 

def fetch_url(url):
    print(f"Fetching {url}...")
    resp = requests.get(url)
    print(f"Finished {url}: {len(resp.text)} bytes")
    # print(f"resp.data {resp.text}")

```
Single Threaded one at time , Sequential Approch 
```python

# --- VERSION 1: Single Threaded (Slow) ---
start = time.time()
for url in urls:
    fetch_url(url)
print(f"Sequential Time: {time.time() - start:.2f}s")
```
Parallel Approch 
```python 
# --- VERSION 2: Multithreaded (Fast) ---
start = time.time()
threads = []
for url in urls:
    # Create a worker for each URL
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

# Wait for all workers to finish
for t in threads:
    t.join()
print(f"Multithreaded Time: {time.time() - start:.2f}s")

```

----


# The GIL (Global Interpreter Lock)
The GIL is a special **"Master Lock"** built into the CPython (standard Python) interpreter.

### **The Difference: GIL vs. Mutex**
**Your Mutex:** Protects your data (e.g., balance = 500).

T**he GIL:** Protects Python's memory. It ensures that only one thread can execute Python bytecode at a time.

Why does it exist? It makes Python's memory management (Reference Counting) simple and fast. The Downside: Even if you have 16 CPU cores, a multithreaded Python program will only use one core at a time for calculation.

## Hard-Coded Example: Race Condition & Fix
Here is a script that demonstrates a Race Condition and how a Mutex (Lock) fixes it.
```Python

import threading

counter = 0
lock = threading.Lock()

def increment_without_lock():
    global counter
    for _ in range(100000):
        # RACE CONDITION: Multiple threads read/write counter simultaneously
        counter += 1
```
Using the __With__ Context Manager For Lock to Release as it Done it work 

read about my [ContextManager](../ContextManager/contextmanager.md)
```python 
def increment_with_lock():
    global counter
    for _ in range(100000):
        # MUTEX FIX: Only one thread can enter this block
        with lock:
            counter += 1
```
```python
# --- TEST 1: The Race ---
counter = 0
threads = [threading.Thread(target=increment_without_lock) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Result without lock: {counter} (Expected 200000)")

# --- TEST 2: The Fix ---
counter = 0
threads = [threading.Thread(target=increment_with_lock) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Result with lock: {counter} (Always 200000)")
```
## When to use Mutithreading vs. Multiprocessing?
- **I/O Bound (Waiting):** Use Multithreading. The GIL is released during waiting (network, file reading), so it works perfectly.

- **CPU Bound (Math/Logic)**: Use Multiprocessing. Each process gets its own GIL and its own CPU core, achieving true parallelism.

---
