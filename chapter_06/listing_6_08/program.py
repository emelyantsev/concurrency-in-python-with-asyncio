import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List


def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(first: Dict[str, int],
                       second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


async def main(partition_size: int):

    with open('/home/aleksey/Downloads/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
    
        contents = []

        count = 0
        for line in f:
            contents.append(line)
            count += 1

            if count == 40000000:
                break

        #contents = f.readlines()

        print( f"the file has {len(contents)} lines" )
    
        loop = asyncio.get_running_loop()
        tasks = []
    
        start = time.time()
    
        with concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

            intermediate_results = await asyncio.gather(*tasks)
            print( f"len intermidiate results == {len(intermediate_results)}" )

            final_result = functools.reduce(merge_dictionaries, intermediate_results)

            print(f"Aardvark has appeared {final_result.get('Aardvark', 0 )} times.")

            end = time.time()
            print(f'MapReduce took: {(end - start):.4f} seconds')


if __name__ == "__main__":

    asyncio.run(main(partition_size=60000))