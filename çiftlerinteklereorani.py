tekler_toplami, ciftler_toplami = 0, 0
girilecek_sayi_sayisi = int(input("Kaç sayi girmek istersiniz: "))
for i in range(1,girilecek_sayi_sayisi+1):
    sayi = int(input(f"{i}. sayiyi giriniz: "))
    if sayi % 2 == 0:
        ciftler_toplami += sayi
    else:
        tekler_toplami += sayi    
ortalama = ciftler_toplami / tekler_toplami
print(ortalama)
