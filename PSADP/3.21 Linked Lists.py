class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        # newnext也是一个Node实例
        self.next = newnext


class UnorderList:
    # 用链表实现无序列表

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        # 创建一个新节点并将插入的元素作为节点的数据
        temp.setNext(self.head)
        # 新插入的节点指向原来的头部（的指向）
        self.head = temp
        # 把头部指向这个新节点

    def size(self):
        # 基于链表的遍历操作， 从头遍历到尾
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                #break    自动braek
            else:
                current = current.getNext()
        return found


    def remove(self, item):

        current = self.head
        previous = None
        found = False
        # 遍历过程中previous总是落后current一个节点

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            # 要移除的元素是列表的第一个，改变链表的头节点
        else:
            previous.setNext(current.getNext())
            # 将要移除的元素之前的元素-->要移除之后的元素

'''
mylist = UnorderList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.search(17)
mylist.remove(93)
mylist.size()
'''

class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count


    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found


    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() >= item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def remove(self, item):

        current = self.head
        previous = None
        found = False
        stop = False

        while not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()

        if stop == True:
            pass
            # 如果没有要找的元素
        else:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())



