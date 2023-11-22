def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def kombinasyon(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))
satir_sayisi = int(input("Satir sayisi: "))
for i in range(0, satir_sayisi):
    for j in range(0, i+1):
        print(int(kombinasyon(i, j)), end=" ")
    print()

