a = int(input())
b = int(input())
il = []

def liczby(a,b,il):
    for x in range(a, b+1):
        if x % 7 == 0 or x % 9 == 0:
            il.append(x)
    print(len(il))
liczby(a,b,il)
