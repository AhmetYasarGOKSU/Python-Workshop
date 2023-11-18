sayi = int(input("Bir sayi giriniz: "))
ilk_sayi = sayi  # En sonda çıktı alırken sayı işlemden geçtiği için ilk sayıyı tut.
kuvvet = 0 
while sayi > 1:
    if sayi % 5 == 0:
        sayi = sayi / 5
        kuvvet += 1 
        if sayi == 1:
            print(f"{ilk_sayi} sayisi 5 in {kuvvet}. kuvvetidir")
    else: 
        print("Sayiniz 5 in bir kuvveti değil")
        break    