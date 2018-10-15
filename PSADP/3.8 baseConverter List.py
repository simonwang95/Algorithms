def baseConverter(decNumber, base):

    digits = "0123456789ABCDE"
    remList = []

    while decNumber > 0:
        rem = decNumber % base
        remList.append(rem)
        decNumber = decNumber // base

    newString = ""
    while len(remList) != 0:
        newString += digits[remList.pop()]

    return int(newString)

print(baseConverter(4, 2))
print(baseConverter(16, 16))
print(baseConverter(100, 8))

