import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['python3', 'chapter_13/listing_13_04/program.py']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE)
    print(f'Process pid is: {process.pid}')

    stdout, stderr = await process.communicate()
    print(stdout)
    print(stderr)
    print(f'Process returned: {process.returncode}')


asyncio.run(main())