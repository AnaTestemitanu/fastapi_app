import aiohttp
import asyncio
from aiohttp import ClientError, ClientResponseError
import certifi
import ssl

# Constant for the maximum number of retries
MAX_RETRIES = 3

ssl_context = ssl.create_default_context(cafile=certifi.where())

# Function to fetch data from a URL with retry logic
async def fetch_data(url, retries=MAX_RETRIES):
    for i in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, ssl=ssl_context) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        raise ClientResponseError(
                            response.request_info,
                            response.history,
                            status=response.status,
                            message=f"Request to {url} failed with status code {response.status}",
                            headers=response.headers
                        )
        except (ClientError, Exception) as e:
            # If this was the last attempt, re-raise the exception.
            if i == retries - 1:
                raise e
            # Implement the exponential backoff.
            else:
                backoff_time = (2 ** i) + (1 if i > 0 else 0)
                await asyncio.sleep(backoff_time)

# Function to fetch users and their posts data
async def fetch_users_posts():
    users_url = 'https://jsonplaceholder.typicode.com/users'
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users, posts = await asyncio.gather(fetch_data(users_url), fetch_data(posts_url))
    return users, posts