def wielokrotność():

    a = int(input())
    b = int(input())

    l = []

    l.append(a)
    l.append(b)

    if max(l) % min(l) == 0:
        print("TAK")
    else:
        print("NIE")

wielokrotność()