def lpierwsza(a):

    if a < 2:

        return False

    if a == 2:

        return True

    n = int(a**0.5)

    for i in range(2,n+1):

        if a % i == 0:

            return False

    return True

w = int(input())

for c in range(w):

    a = int(input())

    if lpierwsza(a) == True:

        print(a)

    else:

        d = 2

        l = []

        while a>1:

            if a % d == 0:

                l.append(d)

                a = a // d
            else:

                d += 1         

        for i in range(len(l)-1):

            print(l[i],end='*')
            
        print(l[-1])