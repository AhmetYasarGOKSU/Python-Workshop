sayi = int(input("Bir sayı giriniz: "))
bolen = 2 
farklibolen = 0

while sayi > 1:
    if sayi % bolen == 0:
        sayi = sayi / bolen 
        if farklibolen != bolen:
            farklibolen = bolen
            print(farklibolen)       
    else:
        bolen = bolen + 1 
