import asyncio


async def loundary():
    print('Начали стирку')
    await asyncio.sleep(7)
    print('Стирка закончена')


async def soup():
    print('начали готовку')
    await asyncio.sleep(6)
    print('Суп готов')


async def tea():
    print('Чайник на плите')
    await asyncio.sleep(2)
    print('Чай готов')


async def main():
    await asyncio.gather(loundary(), soup(), tea())


asyncio.run(main())
