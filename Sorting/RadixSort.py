import random
from timeit import default_timer as timer


# https://www.geeksforgeeks.org/radix-sort/
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
    return arr


def main():
    nums = []
    for x in range(10000):
        nums.append(random.randint(1, 1000000))

    start = timer()
    radixSort(nums)
    end = timer()
    print('Evaluation time: ' + str(end - start) + ' seconds')


if __name__ == "__main__":
    main()
