import asyncio


class Countdown:
    def __init__(self, count, name):
        self.count = count
        self.name = name

    async def start(self):
        sp = []
        for i in range(1, self.count + 1):
            sp.append(self.timer(i))
        await asyncio.gather(*sp)
        print(self.name + ' ok')

    async def timer(self, n):
        await asyncio.sleep(n)
        print(self.name + str(self.count + 1 - n))


async def main():
    cd = Countdown(10, 'First')
    await cd.start()


asyncio.run(main())
