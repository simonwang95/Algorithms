# 二项堆 实现优先队列
# 最小堆
class BinHeap:

    def __init__(self):
        self.heapList = [0]
        # 存储数据，0数据没有用到
        self.currentsize = 0
        # 二项堆的总节点数，初始为0
        # 表首下标为0的项并没有用到，但为了后面代码可以用到整数乘除法，依然保留

    def percUp(self, i):
        # 数据项上浮，保持堆次序
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                # 如果当前节点数据小于父节点数据
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
                # 交换两个节点的数据
            i = i // 2
            # 继续检查上一个父节点

    def insert(self, k):
        # 向最小堆中插入项，运用上浮方法，先添加在末尾，然后上浮到正确的位置
        self.heapList.append(k)
        self.currentsize += 1
        self.percUp(self.currentsize)

    def percDown(self, i):
        # 节点下沉
        while (i * 2) <= self.currentsize:
            # 当左子节点存在 --> 保证存在最小子节点
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                # 如果当前节点数值小于其最小子节点，二者交换数值
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
            # 继续向下检查，直至没有子节点

    def minChild(self, i):
        # 查找最小子节点，在确保存在的情况下调用
        if i * 2 + 1 > self.currentsize:
            # 如果右子节点不存在 --> 左子节点最小 --> 返回左子节点
            return i * 2
        elif self.heapList[i * 2] < self.heapList[i * 2 + 1]:
            # 如果左子节点数值小于右子节点数值
            return i * 2
        else:
            return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]      # 要被删除的根节点值
        self.heapList[1] = self.heapList[self.currentsize]
        # 用最后一个节点替换根节点
        self.currentsize -= 1
        # 二项堆规模减1
        self.heapList.pop()
        # 删除最后一个节点
        self.percDown(1)
        # 将被替换的根节点下沉
        return retval
        # 返回根节点的值

    ## 找到方法从无序表生成一个二项堆
    def biuldHeap(self, alist):
        i = len(alist) // 2
        # 从树的中间开始，回溯到根节点
        # 因为堆是完全树，任何经过中间点的节点都是叶节点，没有子节点
        self.currentsize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

bh = BinHeap()
bh.biuldHeap([9, 5, 6, 2, 3])
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())



