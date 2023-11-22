sayi_list = [1,4,17,20,24,34,38,41,43,45]
ilk_sayi = 0
son_sayi = len(sayi_list)-1
istenen_sayi = int(input("Aramak istediğiniz sayıyı giriniz: "))
while True:
    ortadaki_sayi = (ilk_sayi + son_sayi) // 2
    if sayi_list[ortadaki_sayi] < istenen_sayi:
        ilk_sayi = ortadaki_sayi + 1
    elif sayi_list[ortadaki_sayi] > istenen_sayi:
        son_sayi = ortadaki_sayi - 1
    else:
        print(f"Aradiğiniz sayi {ortadaki_sayi+1}. sayi")
        break
print(sayi_list.index(24))