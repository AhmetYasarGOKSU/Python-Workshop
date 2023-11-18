import random

tahmin_sayisi = random.randint(1,100)
sayi = int(input("1 ile 100 arasında bir sayı girin: "))
while sayi != tahmin_sayisi:
    sayi = int(input("1 ile 100 arasında bir sayı girin: "))
    if sayi > tahmin_sayisi:
        print("Daha küçük bir sayı girin")
    elif sayi < tahmin_sayisi:
        print("Daha büyük bir sayı girin")    
print("Tebrikler doğru tahmin ettiniz")        