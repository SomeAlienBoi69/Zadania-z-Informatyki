a = input().strip()
b = input().strip()

def anagram(a,b):

    if sorted(a) == sorted(b):
        print("TAK")
    else:
        print("NIE")

anagram(a,b)