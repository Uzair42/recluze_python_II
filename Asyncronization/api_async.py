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