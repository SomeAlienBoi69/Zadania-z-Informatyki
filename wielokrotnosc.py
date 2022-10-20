def wielokrotność():

    a = int(input())
    b = int(input())

    l = []

    l.append(a)
    l.append(b)
    a = max(l)
    b = min(l)
    
    if a % b == 0:
        print("TAK")
    else:
        print("NIE")

wielokrotność()