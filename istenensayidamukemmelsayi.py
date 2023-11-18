istenen_sayi = int(input("Kaç adet mükemmel sayı bulmak istersiniz: "))
kontrol_edilen = 2 
bulunan_sayi = 0
while istenen_sayi > bulunan_sayi:
    toplam = 0 
    for i in range(2,kontrol_edilen // 2 + 1,1):
        if kontrol_edilen % i == 0:
            toplam = toplam + i 
    if kontrol_edilen == toplam:
                bulunan_sayi += 1 
                print(toplam)        
    kontrol_edilen += 1            

