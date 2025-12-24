# Async/Await

## Compare three versions

1. **Synchronous (blocking)** – slow and inefficient.
2. **Threaded** – better, but heavy overhead.
3. **Async/await** – fast, lightweight, and clean.

### Scenario: Download data from multiple websites

Imagine fetching data from 10 slow websites, each taking ~2 seconds to respond.

#### 1. Synchronous Version (Blocking – Very Slow)

```python
import time
import requests

def fetch_sync(url):
    print(f"Starting fetch: {url}")
    response = requests.get(url)
    print(f"Finished fetch: {url}")
    return response.text[:100]  # Just a snippet

def main_sync():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        # ... imagine 10 URLs
    ] * 3  # 9 URLs total

    start = time.time()
    results = [fetch_sync(url) for url in urls]
    end = time.time()

    print(f"\nSynchronous took: {end - start:.2f} seconds")

if __name__ == "__main__":
    main_sync()
```

**Output**: Takes ~18 seconds (9 × 2 seconds), because each request waits for the previous one.

#### 2. Threaded Version (Faster, but Heavy)

```python
import time
import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_sync(url):
    print(f"Starting fetch: {url}")
    response = requests.get(url)
    print(f"Finished fetch: {url}")
    return response.text[:100]

def main_threaded():
    urls = ["https://httpbin.org/delay/2"] * 9

    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_sync, urls))
    end = time.time()

    print(f"\nThreaded took: {end - start:.2f} seconds")

if __name__ == "__main__":
    main_threaded()
```

**Output**: Takes ~2 seconds (parallel), but uses 9 threads → high memory/CPU overhead.

#### 3. Async/Await Version (Best for I/O – Fast & Lightweight)

```python
import asyncio
import aiohttp
import time

async def fetch_async(session, url):
    print(f"Starting fetch: {url}")
    async with session.get(url) as response:
        text = await response.text()
        print(f"Finished fetch: {url}")
        return text[:100]

async def main_async():
    urls = ["https://httpbin.org/delay/2"] * 9

    start = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)  # Run all concurrently
    
    end = time.time()
    print(f"\nAsync took: {end - start:.2f} seconds")
    print(f"Results collected: {len(results)} items")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main_async())
```

**Output**:
- Takes ~2 seconds (same as threads).
- Uses **only 1 thread**.
- Much lower memory usage.
- Clean, readable code.

### Why Redesign to Async/Await?

You should **redesign** from sync → async when:

| Situation                          | Use Sync | Use Threads | Use Async/Await |
|------------------------------------|----------|-------------|-----------------|
| CPU-heavy tasks (e.g., math)       | ✅       | ✅          | ❌              |
| I/O-heavy (network, files, DB)     | ❌       | ✅          | ✅✅ Best       |
| High concurrency (1000+ connections)| ❌       | ❌ (too heavy)| ✅✅ Ideal      |
| Web servers/APIs (FastAPI, etc.)   | ❌       | Limited     | ✅ Standard     |

### How Async Actually Works (Low-Level View in This Example)

1. `async def fetch_async(...)` → creates a **coroutine function**.
2. Calling `fetch_async(...)` → returns a **coroutine object** (not executed yet).
3. `asyncio.gather(*tasks)` → wraps them into **Tasks** and schedules them on the **event loop**.
4. When `await response.text()` is hit:
   - The coroutine **suspends** (pauses without blocking the thread).
   - Control returns to the **event loop**.
   - The event loop checks other tasks or waits for I/O events.
5. When the HTTP response arrives (via OS non-blocking I/O), the event loop **resumes** the coroutine exactly where it left off.
6. All 9 requests run **concurrently** in a single thread.

###  Real-World 

If you have existing sync code like `requests.get()`, you can **gradually redesign**:

```python
# Bad: Mixing sync in async (blocks the event loop!)
async def bad_example():
    requests.get("https://...")  # DON'T do this!

# Good: Use async-compatible libraries
async def good_example():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://...") as resp:
            await resp.text()
```

**Popular async libraries**:
- `aiohttp` → instead of `requests`
- `aiomysql` / `asyncpg` → instead of sync DB drivers
- `aiofiles` → instead of `open()`



#### async/await when ... 
- You're waiting a lot (network, disk, APIs).
- You want to handle hundreds/thousands of concurrent operations.
- You want clean, scalable, efficient code without thread complexity.

