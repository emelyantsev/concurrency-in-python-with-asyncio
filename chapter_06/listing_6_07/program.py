import time

freqs = {}

with open("/home/aleksey/Downloads/googlebooks-eng-all-1gram-20120701-a", encoding='utf-8') as f:
    #lines = f.readlines()

    start = time.time()

    lines_count = 0

    for line in f:     # see https://www.geeksforgeeks.org/how-to-read-large-text-files-in-python/
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] = freqs[word] + count
        else:
            freqs[word] = count

        lines_count += 1

    print(lines_count)

    end = time.time()
    print(f'{end-start:.4f}')