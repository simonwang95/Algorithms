def merge(left, right):
    lst = []
    while left and right:
        if left[0] <= right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    lst = lst + left + right
    return lst

def mergeSort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)

L = [54,26,93,17,77,31,44,55,20]

print(mergeSort(L))