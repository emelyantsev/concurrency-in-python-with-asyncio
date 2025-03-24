import asyncio
 

class CustomAwaitable(object):
    

    def __init__(self, id : int):
        self.id = id

    def __await__(self):
        print(f'Await {self.id} is running')
        yield
        print(f'Await {self.id} is done')
 
async def print_and_sleep():
    for i in range(3):
        print(i)
        await asyncio.sleep(1)
 

async def main1():

    task1 = asyncio.create_task( print_and_sleep() )
    await asyncio.gather( CustomAwaitable(1), task1, CustomAwaitable(2) )

async def main2():

    await CustomAwaitable(1)
    await CustomAwaitable(2)

async def main3():

    task1 = asyncio.create_task( print_and_sleep() )
    await CustomAwaitable(1)
    await CustomAwaitable(2)
    await task1
 

if __name__ == "__main__":

    asyncio.run(main3())