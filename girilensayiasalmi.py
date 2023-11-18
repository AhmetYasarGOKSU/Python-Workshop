sayi = int(input("Bir sayı giriniz: "))
asalkontrol = 0


for i in range(2,sayi//2 + 1,1):
    if sayi % i == 0:
        asalkontrol = 1

if asalkontrol == 1: 
    print("Sayınız asal değil")
else:
    print("Sayınız asal")