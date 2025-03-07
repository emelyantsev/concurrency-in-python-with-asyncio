import asyncio
import os
import tty
from collections import deque
from chapter_08.listing_8_05.program import create_stdin_reader
from chapter_08.listing_8_07.program import *
from chapter_08.listing_8_08.program import read_line
from chapter_08.listing_8_09.program import MessageStore

import termios


async def sleep(delay: int, message_store: MessageStore):
    await message_store.append(f'Starting delay {delay}') #A
    await asyncio.sleep(delay)
    await message_store.append(f'Finished delay {delay}')


async def main():
    tty.setcbreak(sys.stdin)
    os.system('clear')
    rows = move_to_bottom_of_screen()

    async def redraw_output(items: deque): #B
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(redraw_output, rows - 1)

    stdin_reader = await create_stdin_reader()

    try:

        while True:

            line = await read_line(stdin_reader)
            delay_time = int(line)
            asyncio.create_task(sleep(delay_time, messages))

    except Exception:
        pass

    # except KeyboardInterrupt as e:
    #     print("Caught KeyboardInterrupt")

    # except asyncio.CancelledError as e:
    #     print("Caught CancelledError ")

    # finally:

    #     print("performing cleanup")
    #     fd = sys.stdin.fileno()
    #     old = termios.tcgetattr(fd)
    #     old[3] = old[3] | termios.ECHO
    #     termios.tcsetattr(fd, termios.TCSADRAIN, old)


asyncio.run(main())