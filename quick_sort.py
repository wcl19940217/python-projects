def sub_sort(list1, low, height):
    key = list1[low]
    while low < height:
            while low < height and list1[height] >= key:
                height -= 1
            while low < height and list1[height] < key:
                list1[low] = list1[height]
                low += 1
                list1[height] = list1[low]
    list1[low] = key
    return low

# #思路1
# （1）先从数列中取出一个数作为基准数。
# （2）分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
# （3）再对左右区间重复第二步，直到各区间只有一个数。



def quick_sort(list1, low, height):
    if low < height:
        index_key = sub_sort(list1, low, height)
        quick_sort(list1, low, index_key)
        quick_sort(list1, index_key+1, height)


if __name__ == '__main__':
    list1 = [5, 10, 88, 0, 99, 1, 0, 100, 53]
    print(list1)
    quick_sort(list1, 0, len(list1)-1)
    print(list1)
