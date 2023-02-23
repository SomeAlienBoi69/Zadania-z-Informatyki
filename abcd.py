def dzielnik(a):

    y = 0

    pierwiastek = int(a ** 0.5)

    for x in range(1, pierwiastek + 1):

        if a % x == 0:
            y = y + x + a // x

    return y

#a = int(input())

print(dzielnik(1000000000))