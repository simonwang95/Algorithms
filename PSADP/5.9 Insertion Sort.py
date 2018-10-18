def insertionSort(L):
    # 向已排序的子列插入元素，每次排好子列长度加一
    for j in range(1, len(L)):
        # j为插入排序的待插入项
        key = L[j]
        i = j - 1
        # 从待插入的前一项开始检查, 比待插入项大的向后移动一位

        while i >= 0 and L[i] > key:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key       # 插入元素

    return L

L = [54,26,93,17,77,31,44,55,20]
insertionSort(L)
print(L)
