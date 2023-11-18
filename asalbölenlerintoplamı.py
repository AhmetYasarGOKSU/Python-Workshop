bolen = 2 
toplam = 0 
sayi = int(input("Bir sayı giriniz: "))

while sayi>1:
    if sayi % bolen == 0:
        sayi = sayi / bolen
        toplam = toplam + bolen
        print(bolen)
    else:
        bolen = bolen + 1             
print("asal bölenlerin toplamı: ",toplam)