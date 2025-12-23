import threading
import requests
import time

urls = ["https://google.com", "https://python.org", "https://github.com"] 

def fetch_url(url):
    print(f"Fetching {url}...")
    resp = requests.get(url)
    print(f"Finished {url}: {len(resp.text)} bytes")
    # print(f"resp.data {resp.text}")

# --- VERSION 1: Single Threaded (Slow) ---
start = time.time()
for url in urls:
    fetch_url(url)
print(f"Sequential Time: {time.time() - start:.2f}s")

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