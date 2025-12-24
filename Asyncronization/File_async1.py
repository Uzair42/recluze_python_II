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
    files = ['async1.py','async.md']
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