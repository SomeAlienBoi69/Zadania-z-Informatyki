kod = input()
słowo = input()
output = ""

for x in słowo:
    poz = kod.find(x)
    if poz == -1:
        output += x
    elif poz % 3 == 0:
        output += kod[poz + 1]
    else:
        output += kod[poz - 1]

print(output)