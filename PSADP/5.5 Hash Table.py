class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size      # 储存key
        self.data = [None] * self.size       # 储存data(value)

    '''
    散列函数：求余
    冲突解决："+1" 现行探测
    put函数假设最终一定能找到一个能让新的密钥填入的槽。 槽不为空-->rehash 循环-->替换
    '''

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))   # len(self.slots)即self.size

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] == data     # replace (类似对字典键重新赋值)
            else:                                # 槽位已被其他键占用 --> rehash
                nextslot = self.rehash(hashvalue, len(self.slots))      # nextslot --> rehash值
                rehashTime = 1      ###  这个条件为自己添加 防止无限循环(put过多的键值对)
                while self.slots[nextslot] != None and self.slots[nextslot] != key and \
                        rehashTime <= self.size:
                    # rehash对应位置不为空，且键不相同
                    nextslot = self.rehash(nextslot, len(self.slots))
                    # 继续向下rehash
                    rehashTime += 1

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data   # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True   # 确保能够跳出循环，此时返回None
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

