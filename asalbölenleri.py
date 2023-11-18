toplam = 0 
bolen = 2  
sayi = int(input("Bir sayı giriniz: "))


while sayi > 1:
    if sayi % bolen == 0:
        sayi = sayi / bolen
        toplam = toplam + bolen 
        print(bolen) 
    else:
        bolen = bolen + 1 
        