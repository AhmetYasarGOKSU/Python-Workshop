notlar = []
not_toplami = 0
ders_sayisi = int(input("Kaç dersin ortalamasini hesaplayacaksiniz: "))
for i in range(0,ders_sayisi):  
    alinan_not = int(input(f"{i + 1}.dersten aldiginiz not: "))
    notlar.append(alinan_not)
    not_toplami += notlar[i]   
not_ortalamasi = not_toplami / ders_sayisi 
print(f"Not ortalamaniz: {not_ortalamasi}")
