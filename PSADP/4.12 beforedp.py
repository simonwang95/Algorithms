def recDC(coinValueList, change, knownResults):
# Recursively Counting Coins with Table Lookup

    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    # 添加一个测试 检查表中是否包含了为某个特定数目找零的硬币最小值
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins

print(recDC([1, 5, 10, 25], 63, [0] * 64))


def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change + 1):
        coinCount = cents

        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount

    return minCoins[change]