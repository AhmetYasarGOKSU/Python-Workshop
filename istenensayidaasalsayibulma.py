istenen_sayi = int(input("Kaç adet asal sayı bulunmasını istiyorsunuz: "))
kontrol_edilen = 2
bulunan_sayi = 0 
asalkontrol = 0
while istenen_sayi > bulunan_sayi:
    asalkontrol = 0
    for i in range(2,kontrol_edilen // 2 + 1,1):
        if kontrol_edilen % i == 0:
            asalkontrol = 1 
    if asalkontrol == 0:
        print(kontrol_edilen)
        bulunan_sayi += 1
    kontrol_edilen += 1        
