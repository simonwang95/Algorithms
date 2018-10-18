# 原始希尔排序，除2递减。问题：增量不互质，可能不起作用
# 目标：一次交换，消除更多的逆序对

def orginShellSort(L):
    sublistcount = len(L) // 2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(L, startposition, sublistcount)
        print("After increment of size", sublistcount, L)
        sublistcount = sublistcount //2

def gapInsertionSort(L, start, gap):
    for i in range(start + gap, len(L), gap):
        # i 为插入排序的待插入项
        key = L[i]
        j = i - gap
        while j >= 0 and L[j] > key:
            L[j + gap] = L[j]
            j -= gap
        L[j + gap] = key
    return L


def shellSort(L):
    # 其他增量序列 如Hibbard
    hgap = [2**k - 1 for k in range(20, 1, -1) if 2**k -1 < len(L)]
    # 生成Hibbard增量序列，保证相邻互质，保证最大间隔小于列表长度
    # range中的20是一个暂时的办法 生成的最大间隔在百万量级
    for i in range(len(hgap)):
        # 对于每一个间隔  进行一组排序
        currgap = hgap[i]
        for startposition in range(currgap):
            #对于间隔中的每个位置，采用插入排序
            gapInsertionSort(L, startposition, currgap)

    return L


L = [54,26,93,17,77,31,44,55,20]
shellSort(L)
print(L)