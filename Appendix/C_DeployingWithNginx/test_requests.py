import asyncio
import aiohttp
from util import async_timed
from aiohttp import ClientSession

from typing import Tuple

#@async_timed()
async def fetch_status_and_body(session: ClientSession,
                       url: str,
                       delay: int = 0) -> tuple[int, dict] :
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return (result.status, await result.json())


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['http://localhost/info' for _ in range(1000)]
        requests = [fetch_status_and_body(session, url) for url in urls]
        responses = await asyncio.gather(*requests)

        stat = dict()

        for response in responses:

            assert response[0] == 200

            pid = response[1]['pid']
            tid = response[1]['tid']

            assert pid == tid

            stat[pid] = stat.get(pid, 0) + 1
            stat[tid] = stat.get(tid, 0) + 1

        print(stat)


asyncio.run(main())