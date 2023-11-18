toplam = 0 
list = []
for i in range(1,11):
    sayi = int(input(f"{i}.sayiyi giriniz: "))
    toplam += sayi
    list.append(sayi)
enbuyuk_sayi, enkucuk_sayi = list[0], list[0]
for i in range(1,10):
    if list[i] > enbuyuk_sayi:
        enbuyuk_sayi = list[i] 
    if list[i] < enkucuk_sayi:
        enkucuk_sayi = list[i]
tüm_ortalama = toplam / 10 
bk_ortalama = (enbuyuk_sayi + enkucuk_sayi) / 2 # büyük ve küçüğün ortalaması =  bk ortalama         
fark = tüm_ortalama - bk_ortalama
print(f"tüm ortalama ile büyük-küçük ortalamanın farkı : {fark}")
