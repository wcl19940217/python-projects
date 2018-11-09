import math


def print_tree(array):
    index = 1
    depth = math.ceil(math.log2(len(array)))
    print(depth)
    sep = ' '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2**(depth-i-1)-1), end='')
        line = array[index:index+offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth-i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')

        index += offset
        print()


origin = [0, 30, 20, 80, 40, 50, 10, 60, 70, 90]
total = len(origin) - 1
print(origin)
print_tree(origin)
print('++++++++')


def heap_adjust(n, i, array: list):
    while 2 * i <= n:
        lchile_index = 2 * i
        max_child_index = lchile_index
        if n> lchile_index and array[lchile_index + 1] > array[lchile_index]:
            max_child_index = lchile_index + 1

        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index
        else:
            break


def max_heap(total, array:list):
    for i in range(total//2, 0, -1):
        heap_adjust(total, i, array)
    return array


print_tree(max_heap(total, origin))
print('--------------------')


def sort(total, array:list):
    while total > 1:
        array[1], array[total] = array[total], array[1]
        total -= 1
        if total == 2 and array[total] >= array[total-1]:
            break
        heap_adjust(total, 1, array)
    return array


print_tree(sort(total, origin))
print(origin)