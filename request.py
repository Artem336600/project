import requests
import asyncio
import aiohttp


def save(url, name):
    file = open(name, 'wb')
    file.write(requests.get(url).content)
    file.close()


url = 'https://api.thecatapi.com/v1/images/search?limit=10'
response = requests.get(url).json()
sp = []
sp1 = []
for i in range(10):
    sp.append(response[i]['url'])
for j in range(10):
    save(sp[j], 'cat' + str(j) + sp[j][-4:])
