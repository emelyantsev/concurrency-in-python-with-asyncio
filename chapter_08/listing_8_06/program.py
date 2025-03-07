import asyncio
from chapter_08.listing_8_05.program import create_stdin_reader
from util import delay


async def main():
    stdin_reader = await create_stdin_reader()
    
    print('Enter a time to sleep:')

    while delay_time := await stdin_reader.readline():
        asyncio.create_task(delay(int(delay_time)))
        print('Enter a time to sleep:')

asyncio.run(main())