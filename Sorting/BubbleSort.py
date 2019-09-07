import random
from timeit import default_timer as timer


def bubbleSort(arr):
    while True:
        flag = True
        for y in range(1, len(arr)):
            if arr[-y] < arr[-y - 1]:
                flag = False
        for x in range(len(arr) - 1):
            if arr[x] > arr[x + 1]:
                tem = arr[x]
                arr[x] = arr[x + 1]
                arr[x + 1] = tem
        if flag:
            break


def main():
    f = open('text.txt', 'a')

    nums = []
    for x in range(10000):
        nums.append(random.randint(1, 1000000))
    start = timer()
    bubbleSort(nums)
    end = timer()
    print('Evaluation time: ' + str(end - start) + ' seconds')
    a.write('Bubblesort evaluation time: ' + str(end - start) + ' seconds')


if __name__ == "__main__":
    main()