import textwrap

słowo = input()

def szyfr(słowo):

    sw = textwrap.wrap((słowo), 2)
    a = []

    for x in sw:
        x = x[::-1]
        a.append(x)

    sh = " ".join(a)

    print(sh)

szyfr(słowo)