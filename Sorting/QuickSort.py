import random
from timeit import default_timer as timer


# https://www.geeksforgeeks.org/quick-sort/
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def main():

    f = open('test.txt', 'a')

    nums = []
    for x in range(10000):
        nums.append(random.randint(1, 1000000))

    start = timer()
    quickSort(nums, 0, len(nums) - 1)
    end = timer()
    print('Evaluation time: ' + str(end - start) + ' seconds')
    f.write('Quicksort evaluation time: ' + str(end - start) + ' seconds\n')
    f.close()

if __name__ == "__main__":
    main()