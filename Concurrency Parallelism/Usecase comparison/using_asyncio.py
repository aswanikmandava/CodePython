import os
import requests
import json
import time
import asyncio
import aiohttp
import aiofiles
import sys

"""
Event loops are constructs inherent to asynchronous programming that allow performing tasks asynchronously.

To call an async function, you must either use the await keyword from another async function or call create_task() directly 
from the event loop, which can be grabbed from asyncio.get_event_loop()
    async with allows awaiting async responses and file operations.
    async for (not used here) iterates over an asynchronous stream.

An event loop is a process that waits around for triggers and then performs specific (programmed) actions once those triggers are met.
They often return a "promise" (JavaScript syntax) or "future" (Python syntax) of some sort to denote that a task has been added. 
Once the task is finished, the promise or future returns a value passed back from the called function (assuming the function does return a value).

The idea of performing a function in response to another function is called a "callback."
"""

async def write_genre(filename):
    """
    Get a random genre using REST endpoint

    We're using async with to open our client session asynchronously. 
    The aiohttp.ClientSession() class is what allows us to make HTTP requests and remain connected to a source 
    without blocking the execution of our code. We then make an async request to the Genrenator API and 
    await the JSON response (a random music genre). In the next line, we use async with again with the 
    aiofiles library to asynchronously open a new file to write our new genre to. We print the genre, then write it to the file.

    Unlike regular Python scripts, programming with asyncio pretty much enforces* using some sort of "main" function.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
    async with aiohttp.ClientSession() as client_session:
        async with client_session.get(url=url, headers=headers) as r:
            response = await r.json()

    async with aiofiles.open(filename, "w") as fh:
        print(f"writing genre {response} to {filename}")
        await fh.write(response)

async def main():
    tasks = []
    for i in range(5):
        filename = f"genre-{i}.txt"
        tasks.append(write_genre(filename))
    """
    We append our tasks to our list, but they are not actually run yet. 
    The calls don't actually get made until we schedule them with await asyncio.gather(*tasks).
    This runs all of the tasks in our list and waits for them to finish before continuing with the rest of our program. 
    """
    await asyncio.gather(*tasks)


# Lastly, we use asyncio.run(main()) to run our "main" function. The .run() function is the entry point for our program
if __name__ == '__main__':
    start_time = time.time()
    pid = os.getpid()
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end_time = time.time()
    print(f"{pid} Execution took {(end_time - start_time)} secs")