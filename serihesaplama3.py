total = 0 
def seri(n):
    global total
    for i in range(1,n+1):
        total += i-(i+1)
    return total
seri_sayisi = int(input("Seri sayisi: "))
seri(seri_sayisi)
print(total)    
