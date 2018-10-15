from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binSring = ''
    while not remstack.isEmpty():
        binSring = binSring + str(remstack.pop())

    return binSring

print(divideBy2(42))

# 和用列表直接实现思路一致