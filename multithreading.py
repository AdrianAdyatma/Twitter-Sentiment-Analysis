import time
import threading
import multiprocessing


def square(numbers):
    print("square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n * n)


def cube(numbers):
    print("cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n * n * n)


arr = [2, 3, 8, 9]

t = time.time()

# square(arr)
# cube(arr)

print("Done in:", time.time() - t)
