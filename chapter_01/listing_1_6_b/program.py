import multiprocessing
import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) is {fib(number)}')


def fibs_with_multiprocessing():
    p1 = multiprocessing.Process(target=print_fib, args=(37,))
    p2 = multiprocessing.Process(target=print_fib, args=(38,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


start_processes = time.time()

fibs_with_multiprocessing()

end_processes = time.time()

print(f'Prosesses took {end_processes - start_processes:.4f} seconds.')