def szyfrowanie(słowo, klucz):
    klucz = klucz % 26
    w = ""
    for litera in słowo:
        poz = ord(litera) + klucz
        if poz > 90:
            poz = poz - 26
        w = w + chr(poz)
    return w

def odszyfrowanie(słowo, klucz):
    klucz = klucz % 26
    w = ""
    for litera in słowo:
        poz = ord(litera) + klucz
        if poz < 65:
            poz = poz + 26
        w = w + chr(poz)
    return w


słowo = input().upper()
klucz = int(input())

print(szyfrowanie(słowo, klucz))
print(odszyfrowanie(słowo, klucz))