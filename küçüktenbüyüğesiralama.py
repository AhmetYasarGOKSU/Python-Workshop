Sayilar = [55,50,70,2,10,6]

for i in range(0,len(Sayilar)): 
    for j in range(i+1,len(Sayilar)): 
        if Sayilar[i] > Sayilar[j]:
            Sayilar[i], Sayilar[j] = Sayilar[j], Sayilar[i]

print(Sayilar)

