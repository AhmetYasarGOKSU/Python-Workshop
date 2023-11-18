sayi = int(input("Bir tamsayı giriniz: "))
toplam = 0 

for i in range(1,sayi+1,1):
    if i % 2 == 0:
        toplam = toplam + i

print("1'den girdiğiniz sayıya kadar olan sayılardan çift olanların toplamı:",toplam)

    