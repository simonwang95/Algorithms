def qsort(L):
    if len(L) <= 1:
        return L
    return qsort([x for x in L[1:] if x <= L[0]]) + L[0:1] + qsort([y for y in L[1:] if y > L[0]])
    # L[0:1]表示一个元素的列表 而不是一个元素
    # <= 和 > 而不是 < 和 >  可以排重复


def quickSort(alist):
    # 为递归函数写出标准接口
    return quickSortHelper(alist, 0, len(alist) - 1)


def median3(alist, first, last):
    # 选择pivot为列表首中尾的中位数，并储存于列表头部（三者最大值在列表末尾）

    middle = (first + last) // 2
    if alist[first] > alist[middle]:
        alist[first], alist[middle] = alist[middle], alist[first]
    if alist[first] > alist[last]:
        alist[first], alist[last] = alist[last], alist[first]
    if alist[middle] > alist[last]:
        alist[middle], alist[last] = alist[last], alist[middle]
    # 将三者从小到大排序

    alist[first], alist[middle] = alist[middle], alist[first]
    # 将中位数与最小值互换
    return alist[first]


def quickSortHelper(alist, first, last):

    if first < last:

        pivot = median3(alist, first, last)
        #pivot = alist[first]    # 选取列表第一个元素为主元
        #pivot = alist[0] ---> 左右两侧分别排序（误）
        # 基准pivot，此时pivot位于列表头部
        leftmark = first + 1
        rightmark = last
        # 初始化左右指针
        done = False
        # 为pivot找到正确的位置，且将列表（根据pivot的大小）分割为两个部分
        while not done:
            while leftmark <= rightmark and alist[leftmark] <= pivot:
                leftmark += 1
                # 左指针向右移动，仅在左边出现大于pivot时，跳出此循环 --> 进行检查或交换
            while rightmark >= leftmark and alist[rightmark] >= pivot:
                rightmark -= 1
            if leftmark > rightmark:
                done = True
            else:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

        # 将pivot放到正确的位置，此时为rightmark，leftmark指向了rightmark后面一位
        alist[rightmark], alist[first] = alist[first], alist[rightmark]

        quickSortHelper(alist, first, rightmark - 1)
        quickSortHelper(alist, rightmark + 1, last)

    return alist

import random
lst = []
for i in range(100):
    lst.append(random.randint(1,500))
#lst = [3, 2, 40, 50, 6, 37 , 18, 56, 43]
print(qsort(lst))
print(quickSort(lst))