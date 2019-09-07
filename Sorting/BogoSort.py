import random
from timeit import default_timer as timer

def isSorted(list):
    for x in range(len(list)):
        if x == len(list) - 1:
            break
        if list[x + 1] < list[x]:
            return False
    return True





# for y in range(10):
#     f = open('test.txt', 'a')
#     list = []
#     iterations = 0
#
#     for x in range(y):
#         list.append(random.randint(0,100))
#
#     start = timer()
#     while True:
#         random.shuffle(list)
#         iterations += 1
#         if isSorted(list):
#             break
#
#     end = timer()
#     f.write('Sort took ' + str(end - start) + ' seconds with ' + str(y) + ' elements with ' + str(iterations) + ' iterations and a cumulative elapsed time of ' + str(end - abs_start) + '\n')
#     print('Sort took ' + str(end - start) + ' seconds with ' + str(y) + ' elements with ' + str(iterations) + ' iterations and a cumulative elapsed time of ' + str(end - abs_start))
#     f.close()

def bogoSort(arr):
    while True:
        if isSorted(arr):
            break
        else:
            random.shuffle(arr)
    return arr

