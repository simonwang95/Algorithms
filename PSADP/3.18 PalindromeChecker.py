from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
        return stillEqual


def palchecker2(aString):

    aString = aString.strip()
    flag = True
    l = len(aString)

    for i in range(l):
        if aString[i] != aString[l - i - 1]:
            flag = False
            break
    return flag

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print('-------')
print(palchecker2("lsdkjfskf"))
print(palchecker2("radar"))
