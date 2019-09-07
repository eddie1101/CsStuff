import BogoSort
import BubbleSort
import QuickSort
import RadixSort
import random
from timeit import default_timer as timer

def main():
    ori_arr = [random.randint(1, 10000) for x in range(2000)]

    arr = ori_arr
    start = timer()
    bub = BubbleSort.bubbleSort(arr)
    end = timer()

    f = open('data.txt', 'w')
    f.write('SORT BUBBLE WITH ARRAY:\n' + str(ori_arr) + '\nRESULT:\n' + str(bub) + '\nIN TIME:\n' + str(end - start) + '\n')
    f.close()

    arr = ori_arr[:10]
    start = timer()
    bog = BogoSort.bogoSort(arr[:10])
    end = timer()

    f = open('data.txt', 'a')
    f.write('SORT BOGO WITH ARRAY:\n' + str(ori_arr[:10]) + '\nRESULT:\n' + str(bog) + '\nIN TIME:\n' + str(end - start) + '\n')
    f.close()

    arr = ori_arr[:1000]
    start = timer()
    quk = QuickSort.quickSortCaller(arr, 0, len(arr) - 1)
    end = timer()

    f = open('data.txt', 'a')
    f.write('SORT QUICK WITH ARRAY:\n' + str(ori_arr) + '\nRESULT:\n' + str(quk) + '\nIN TIME:\n' + str(end - start) + '\n')
    f.close()

    arr = ori_arr
    start = timer()
    rad = RadixSort.radixSort(arr)
    end = timer()

    f = open('data.txt', 'a')
    f.write('SORT RADIX WITH ARRAY:\n' + str(ori_arr) + '\nRESULT:\n' + str(rad) + '\nIN TIME:\n' + str(end - start) + '\n')
    f.close()

    process_times = []
    total_time = 0
    f = open('data.txt', 'a')
    f.write('MULTIRUN 100 RADIX WITH ARRAY:\n' + str(ori_arr) + '\n')
    for x in range(100):
        arr = ori_arr
        start = timer()
        RadixSort.radixSort(arr)
        end = timer()
        process_times.append(end - start)
        total_time += process_times[x]
        f.write('ITER ' + str(x) + ':\n' + str(process_times[x]) + '\n')
    avg = 0
    for x in process_times:
        avg += x
    avg /= len(process_times)
    f.write('AVERAGE TIME:\n' + str(avg) + '\nTOTAL TIME:\n' + str(total_time) + '\n')
    f.close()

    process_times = []
    total_time = 0
    f = open('data.txt', 'a')
    f.write('MULTIRUN 100 QUICK WITH ARRAY:\n' + str(ori_arr) + '\n')
    for x in range(100):
        arr = ori_arr[:1000]
        start = timer()
        QuickSort.quickSortCaller(arr, 0, len(arr) - 1)
        end = timer()
        process_times.append(end - start)
        total_time += process_times[x]
        f.write('ITER ' + str(x) + ':\n' + str(process_times[x]) + '\n')
    avg = 0
    for x in process_times:
        avg += x
    avg /= len(process_times)
    f.write('AVERAGE TIME:\n' + str(avg) + '\nTOTAL TIME:\n' + str(total_time) + '\n')
    f.close()
    f = open('data.txt', 'r')
    data = f.read()
    f.close()
    print(data)

if __name__ == "__main__":
    main()
