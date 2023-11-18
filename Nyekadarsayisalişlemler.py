sayi = int(input("Bir sayi giriniz: "))
cift_karetoplam = 0 
tek_toplam = 0 
tek_carpim = 1 
for i in range(1,sayi+1):
    if i % 2 == 0:
        cift_karetoplam += i**2
    else:
        tek_carpim = tek_carpim * i
        tek_toplam += i
print(f"Çift sayilarin karelerinin toplami: {cift_karetoplam}")
print(f"Tek sayilarin toplami: {tek_toplam}")
print(f"Tek sayilarin çarpimi: {tek_carpim}")