sifrelenecek_kelime = input("Kelimeyi giriniz: ")
sifreli_kelime = ""
for i in range(0,len(sifrelenecek_kelime)):
    sifre = ord(sifrelenecek_kelime[i]) + 5
    sifreli_kelime += chr(sifre)
print(sifreli_kelime)    


