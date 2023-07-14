import aiohttp
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
url = 'https://api.thecatapi.com/v1/images/search?limit=10'
response = await session.get(url)
cat = response[0]['url']
print(cat)
