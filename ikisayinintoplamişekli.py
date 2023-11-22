sayi = int(input("Sayi giriniz: "))
sayi_list = [1,3,4,5,8,9,20,30,7]
bulundu = False
for i in range(0,len(sayi_list)):
    for j in range(i+1,len(sayi_list)):
        if sayi_list[i] + sayi_list[j] == sayi:
            print(f"listedeki {sayi_list[i]} ve {sayi_list[j]} sayilarinin toplami {sayi} sayisina esittir.")
            bulundu = True
            continue
        else:
            continue
if bulundu != True:
    print("Sayi bulunamadi.")

    


 
 