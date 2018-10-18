def selectionSort(aList):

    for i in range(len(aList) - 1):
        # i从0向后推进，每推进一位，排好一个数
        minIndex = i
        minValue = aList[i]
        # 假设i指向的数为最小值，记录其值和索引，向后遍历查找更小的值

        for j in range(i + 1, len(aList)):
            if minValue > aList[j]:
                minIndex = j
                minValue = aList[j]
        aList[i], aList[minIndex] = aList[minIndex], aList[i]

    return aList

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
