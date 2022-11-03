def horner(s, p):
    w = 0

    for el in s:
        c = ord(el) - 48
        if c >= 1 and c <= 9:
            c = ord(el) - 48
        else:
            c = ord(el) - 55
        
        w = w * p + c

    return w

print(horner("2C", 16))