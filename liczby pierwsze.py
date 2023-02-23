L = [0, 0]

def liczbapierwsza():
    
    for i in range(2, 1001):
        L.append(1)
    
    pierwiastek = int(1001 ** 0.5)

    for i in range(2, pierwiastek + 1):
        if L[i] == 1:
            j = i ** 2

            while j < 1001:
                
                L[j] = 0
                j += 2

liczbapierwsza()

n = int(input())

if L[n] == 1:
    print("Liczba pierwsza")