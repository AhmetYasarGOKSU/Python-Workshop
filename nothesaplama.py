vize = int(input("Vize notunuzu giriniz = "))
final = int(input("Final notunuzu giriniz = "))
ortalama = vize * 30 / 100 + final * 70 / 100 

if ortalama >= 50 and final >= 50:
    print("tebrikler geçtiniz")

else:
    print("maalesef kaldınız")