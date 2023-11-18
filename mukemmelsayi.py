sayi = int(input("Bir sayı giriniz: "))
toplam = 0 
for i in range(1,sayi//2 + 1,1):
    if sayi % i == 0:
        toplam = toplam + i 
    else:
        i += 1
if toplam == sayi:
    print(sayi,"sayısı bir mükemmel sayıdır.")
else:
    print(sayi,"sayısı bir mükemmel sayı değildir.")
