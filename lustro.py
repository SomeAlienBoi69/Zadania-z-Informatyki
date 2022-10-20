liczba = input()
ll = []
def lustro(liczba, ll):
    ll = [int(liczba) for liczba in str(liczba)]
    ll = [x for x in ll if x != 0]
    ll = [str(x) for x in ll]
    ll = ll[::-1]
    liczba = "".join(ll)
    print(liczba)
lustro(liczba, ll)