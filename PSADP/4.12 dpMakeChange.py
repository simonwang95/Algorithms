def dpMakeChange(coinValueList, change):
    '''

    :param coinValueList: list of coin values
    :param change: int
    :return:
    '''

    minCoins = [0 for _ in range(change + 1)]
    coinsList = [0 for _ in range(change + 1)]
    # 外层for循环运行完，minCoins会包含从0到需要兑换的数值中每一个值对应的最优解
    # coinsList 包含每一个值对应的新增硬币值（但无法看出减少了哪些硬币），硬币组合需要再计算，0的时候也是1

    for cents in range(change + 1):
        # 从0开始计算  第二个循环j自动排除0
        coinCount = cents
        newCoin = 1   # 新增硬币

        # 下面的循环考虑所有可能的硬币面值来为cents中所指定的数值兑换货币
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                # 体现动态规划，从之前（但不只是前一次）的最优情况考虑-->变化能否带来优化
                coinCount = minCoins[cents - j] + 1
                newCoin = j

        minCoins[cents] = coinCount
        coinsList[cents] = newCoin

    # 计算硬币组合 coinsUsed
    coinsUsed = []
    coin = change    # 剩余面值
    while coin > 0:
        thisCoin = coinsList[coin]
        coinsUsed.append(thisCoin)
        coin = coin - thisCoin

    return minCoins[change], coinsUsed

#dpMakeChange([1, 5, 10, 25], 63)
print(dpMakeChange([1, 5, 10, 25], 63))
print(dpMakeChange([1, 5, 10, 21, 25], 63))