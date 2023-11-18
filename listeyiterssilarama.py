sayilar = [2,3,4,5,1]
gecici_deger = 0
for i in range(0,len(sayilar) // 2):
    sayilar[i], sayilar[len(sayilar)- 1 - i] = sayilar[len(sayilar)- 1 - i], sayilar[i]
print(sayilar)     