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