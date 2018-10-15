def hotPotato(namelist, num):

    simlist = []

    for name in namelist:
        simlist.insert(0, name)

    while len(simlist) > 1:
        for i in range(num):
            simlist.insert(0, simlist.pop())
        simlist.pop()

    return simlist.pop()

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))