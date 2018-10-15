class Fraction:
    def __init__(self, top, bottom):
        '''
        :param top:
        :param bottom:
        '''
        assert type(top) == type(bottom) == int
        assert top >= 0 and bottom > 0

        def gcd(m, n):
            # 欧几里得算法求最大公约数
            while m % n != 0:
                oldm, oldn = m, n
                m = oldn
                n = oldm % oldn
            return n
        # gcd 在构造函数内部/类的外部

        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        #common = gcd(newnum, newden)   已在构造函数中实现
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)

    def __eq__(self, other):
        # 定义一种数值上的相等
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum



def main():

    f1 = Fraction(1, 4)
    f2 = Fraction(1, 2)
    f3 = f1 + f2
    print(f3)
    print(f3 == Fraction(6, 8))

#main()


