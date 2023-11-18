sayi1 = int(input("Birinci sayıyı girin: ")) # sayi1'i gir
sayi2 = int(input("İkinci sayıyı girin: ")) # sayi2'yi gir
sayac = 0 # sayac'ı 0 yap
while sayi2 > 0: # Eğer sayi2 > 0 ise
    sayac = sayac + sayi1 # sayac = sayac + sayi1 yap
    sayi2 = sayi2 - 1 # sayi2 = sayi2 - 1 yap
print("Çarpım sonucu:", sayac) 