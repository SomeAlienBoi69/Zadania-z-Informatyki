def naP(n, p):
    w = ""

    while (n > 0):
        r = n % p

        n = n // p

        if r < 10:
            c = chr(r+48)
    
        else:
            c = chr(r + 55)
    
        w = c + w

    return w


print(naP(31, 16))