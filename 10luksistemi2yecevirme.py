sayi = int(input("Bir sayı giriniz: "))
ikiliksistem = ""
while sayi > 1:
    kalan = sayi % 2
    sayi = (sayi) // 2
    ikiliksistem = str(kalan) + ikiliksistem
ikiliksistem = "1" + ikiliksistem
print(ikiliksistem)

