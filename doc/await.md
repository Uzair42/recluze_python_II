# Real-Life Examples of Async/Await in Python

Here are three additional real-life examples of using `async`/`await` in Python. These build on the previous HTTP fetching example and demonstrate practical scenarios like concurrent API calls, asynchronous file I/O, and a basic async web server. Each example includes:

- A brief description of the use case.
- The full code with **line-by-line comments** explaining what's happening.
- Why async/await is beneficial here.

These use Python 3.7+ and require installing async libraries via pip (e.g., `pip install aiohttp aiofiles` for the first two; `aiohttp` for the third). Run them with `asyncio.run(main())`.

## Example 1: Concurrent API Calls to Weather Service
**Use Case**: Fetch weather data for multiple cities simultaneously from an API (e.g., OpenWeatherMap). This is common in apps that aggregate data from external services. Async allows fetching all at once without blocking, reducing total time from sequential waits.

```python
import asyncio  # Import the asyncio module for async operations.
import aiohttp  # Import aiohttp for asynchronous HTTP requests.

async def fetch_weather(session, city, api_key):
    # Define an async function to fetch weather for a single city.
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    # Construct the API URL with the city and API key.
    async with session.get(url) as response:
        # Use async with to make a non-blocking GET request.
        if response.status == 200:
            # Check if the response status is OK (200).
            data = await response.json()
            # Await the JSON parsing, which is also async.
            return f"{city}: {data['weather'][0]['description']}"
            # Return a formatted string with the weather description.
        else:
            # Handle error if status is not 200.
            return f"{city}: Error {response.status}"
            # Return an error message.

async def main():
    # Define the main async function to orchestrate the tasks.
    api_key = "your_openweathermap_api_key_here"  # Replace with your actual API key.
    # Set the API key (get one from openweathermap.org).
    cities = ["London", "New York", "Tokyo", "Sydney", "Berlin"]
    # List of cities to fetch weather for.
    
    async with aiohttp.ClientSession() as session:
        # Create an async HTTP session for reusing connections.
        tasks = [fetch_weather(session, city, api_key) for city in cities]
        # Create a list of coroutine tasks, one for each city.
        results = await asyncio.gather(*tasks)
        # Await gather to run all tasks concurrently and collect results.
    
    for result in results:
        # Loop through the results after all are complete.
        print(result)
        # Print each weather result.

if __name__ == "__main__":
    # Standard Python idiom to run the script.
    asyncio.run(main())
    # Run the main coroutine in an event loop.
```

**Output Example** (with a valid API key):
```
London: clear sky
New York: few clouds
Tokyo: light rain
Sydney: broken clouds
Berlin: overcast clouds
```
**Why Async?** If done synchronously, this would take ~1-2 seconds per city (5-10s total). Async finishes in the time of the slowest request (~2s), ideal for microservices or dashboards.

## Example 2: Asynchronous File I/O for Reading Multiple Files
**Use Case**: Read and process multiple large log files concurrently (e.g., in a monitoring tool). Async file I/O prevents blocking the main thread during disk reads, useful for servers handling files while staying responsive.

```python
import asyncio  # Import asyncio for event loop and coroutines.
import aiofiles  # Import aiofiles for asynchronous file operations.

async def read_file(filename):
    # Define an async function to read a single file.
    try:
        # Start a try block for error handling.
        async with aiofiles.open(filename, mode='r') as f:
            # Open the file asynchronously in read mode.
            content = await f.read()
            # Await the read operation, which yields if blocked.
            lines = len(content.splitlines())
            # Count the number of lines in the content.
            return f"{filename} has {lines} lines."
            # Return a summary string.
    except FileNotFoundError:
        # Catch if the file doesn't exist.
        return f"{filename} not found."
        # Return an error message.

async def main():
    # Define the main async function.
    files = ["log1.txt", "log2.txt", "log3.txt"]
    # List of file names to read (create these files for testing).
    
    tasks = [read_file(file) for file in files]
    # Create tasks for each file read.
    results = await asyncio.gather(*tasks)
    # Run all reads concurrently and gather results.
    
    for result in results:
        # Iterate over the results.
        print(result)
        # Print each file's summary.

if __name__ == "__main__":
    # Run guard.
    asyncio.run(main())
    # Execute the main function.
```

**Output Example** (assuming files exist):
```
log1.txt has 100 lines.
log2.txt has 250 lines.
log3.txt has 50 lines.
```
**Why Async?** Synchronous `open()`/`read()` would block for each file, especially on slow disks. Async allows overlapping I/O waits, speeding up batch processing in tools like data analyzers or ETL pipelines.

## Example 3: Simple Async Web Server with aiohttp
**Use Case**: Build a basic API server that handles multiple requests concurrently (e.g., a microservice endpoint). Async servers like this power frameworks like FastAPI, handling high traffic without threads.

```python
import asyncio  # Import for async support.
from aiohttp import web  # Import aiohttp's web module for server setup.

async def handle(request):
    # Define an async handler for incoming requests.
    name = request.match_info.get('name', "Anonymous")
    # Get the 'name' parameter from the URL, default to "Anonymous".
    text = f"Hello, {name}!"
    # Create a greeting message.
    await asyncio.sleep(1)  # Simulate a 1-second async delay (e.g., DB query).
    # Await sleep to yield control, allowing other requests to process.
    return web.Response(text=text)
    # Return an HTTP response with the text.

async def main():
    # Define the main function to set up the server.
    app = web.Application()
    # Create a new web application instance.
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    # Add routes: '/' and '/{name}' both map to the handle function.
    runner = web.AppRunner(app)
    # Create a runner to manage the app.
    await runner.setup()
    # Await setup to prepare the server.
    site = web.TCPSite(runner, 'localhost', 8080)
    # Bind the site to localhost:8080.
    await site.start()
    # Start the server asynchronously.
    print("Server started at http://localhost:8080")
    # Print a startup message.
    await asyncio.Event().wait()  # Keep the server running indefinitely.
    # Use an Event to block forever (server runs in background).

if __name__ == "__main__":
    # Run guard.
    asyncio.run(main())
    # Run the server.
```

**How to Test**: Run the script, then visit `http://localhost:8080/Alice` in a browser (outputs "Hello, Alice!"). Open multiple tabs—requests handle concurrently despite the simulated delay.

**Why Async?** Traditional servers (e.g., Flask) block per request. Async handles 1000s of connections in one thread, perfect for chat apps, real-time APIs, or IoT backends. The `await sleep` shows yielding for other tasks.

