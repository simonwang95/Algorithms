class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        # 写了一个使用尚不存在的代码的方法 在各种门中定义具体行为
        return self.output


class BinaryGate(LogicGate):

    # 两条输入行 得到值
    def __init__(self,n):
        #LogicGate.__init__(self, n)
        super(BinaryGate, self).__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        # if - else 结构为了实现连接器，下同
        # 通过getOutPut() -> performGateLogic() 中调用
        if self.pinA == None:
            return int(input("Enter Pin A input for gate" + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source = 'egg'):
        # source 只是一个标记符号，代表已经被占用，可以不用赋值
        # 这个函数从Connector中调用，将pin关联到了一个Connector的实例中
        # 在getPinA/B中，通过Connector实例调用getFrom(self)找到对应的门 调用getOutPut()获得其输出作为输入
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    # 与门 继承了两条输入行和一个标签，并未提供任何新数据
    def __init(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        # 执行之前描述的布尔运算
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    # 或门
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):
    # 一条输入行
    def __init__(self, n):
        LogicGate.__init__(self, n)
        #super(UnaryGate, self).__init__(n)
        # super 代替对父类精确命名 更为普遍的机制
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source = 'burger'):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):
    # 非门
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        return 0 if self.getPin() else 1

    '''
    def performGateLogic(self):
    if self.getPin():
        return 0
    else:
        return 1
    '''

class Connector:
    # 连接器 组合非继承逻辑门
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)
        # 创建实例时即调用，将tgate和此连接器实例相关联

    def getFrom(self):
        return self.fromgate
    # 在getPin(A/b) 中调用(not None 时)

    def getTo(self):
        return self.togate


def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1, g3)
   c2 = Connector(g2, g3)
   c3 = Connector(g3, g4)
   print(g4.getOutput())

main()


