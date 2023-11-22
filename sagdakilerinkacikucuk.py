sayi_list = [7,12,6,3,5,15]
sonuc_list= []
for i in range(0, len(sayi_list)):
    kaci_kucuk = 0
    for j in range(i+1, len(sayi_list)):
        if sayi_list[i] > sayi_list[j]:
            kaci_kucuk += 1
        else:
            continue    
    sonuc_list.append(kaci_kucuk)
print(sonuc_list)