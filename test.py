import aiohttp
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
url = 'https://api.thecatapi.com/v1/images/search?limit=10'


async def download(session, url, n):
    print(f'cat{n} start download')
    response = await session.get(url)
    response_bytes = await response.read()

    with open(f'cats/cat{n}{url[-4:]}', 'wb') as file:
        file.write(response_bytes)
    print(f'cat{n} done!')


async def main():

    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        response_json = await response.json()

        url_cats = []
        for data in response_json:
            url_cats.append(data['url'])

        tasks = []
        for i in range(10):
            tasks.append(download(session, url_cats[i], i))
        await asyncio.gather(*tasks)

        response.release()

def sync_main():
    asyncio.run(main())


sync_main()
