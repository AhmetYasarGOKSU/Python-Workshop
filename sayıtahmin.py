import random

tahmin_sayisi = random.randint(1,100)
sayi = int(input("1 ile 100 arasinda bir sayi girin: "))
while sayi != tahmin_sayisi:
    sayi = int(input("1 ile 100 arasinda bir sayi girin: "))
    if sayi > tahmin_sayisi:
        print("Daha küçük bir sayi girin")
    elif sayi < tahmin_sayisi:
        print("Daha büyük bir sayi girin")    
print("Tebrikler doğru tahmin ettiniz")        