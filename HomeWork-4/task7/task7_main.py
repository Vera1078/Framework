# Напишите программу на Python, которая будет находить сумму элементов массива из 1_000_000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность
# В каждом решении нужно вывести время выполнения вычислений.


from task7_3 import method_threading
from task7_2 import method_multiprocessing
from task7_1 import method_asinc
import asyncio
import time
import random


def sum_item(arr):
    start_time = time.time()
    res = 0
    for i in arr:
        res += i
    print(f'Method synchronous: time - {time.time() - start_time:.5f} sec.')
    print(res)


if __name__ == '__main__':
    start_time = time.time()
    arr = [random.randint(1, 100) for _ in range(100_000_000)]
    print(f'Fill array: time - {time.time() - start_time:.5f} sec.')
    sum_item(arr)
    method_threading(arr)
    method_multiprocessing(arr)
    asyncio.run(method_asinc(arr))


# Fill array: time - 232.52694 sec.
# Method synchronous: time - 14.05553 sec.
# 5050713403
# Method threading: time - 14.70276 sec.
# 5050713403
# Method multiprocessing: time - 33.62783 sec.
# 5050713403
# Method asyncio: time - 20.33869 sec.
# 5050713403