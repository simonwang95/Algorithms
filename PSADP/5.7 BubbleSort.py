def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
    # 降序排列 从n-1到1，共n-1个数，代表需要交换的数对数量
        for i in range(passnum):
        # 从0到passnum - 1
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


def shortBubbleSort(alist):
    # 发现列表已排好时立即结束--->短路冒泡排序
    exchanges = True
    passnum = len(alist) - 1

    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                passnum -= 1
    return alist

# 优点：可以对链表进行排序/不止针对数组
# 交换一次元素，消灭一个逆序对
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

'''
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
'''
