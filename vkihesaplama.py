boy = float(input("Boyunuzu giriniz (m)= "))
kilo = float(input("Kilonuzu giriniz (kg)= "))

vki = kilo / boy**2 

if vki < 18.5:
    print("Çok zayıfsınız")

elif vki >= 18.5 and vki < 25:
    print("Sağlıklısınız")

elif vki >=25 and vki < 30:
    print("Fazla kilolusunuz")

elif vki >=30 and vki < 35:
    print("1.Derece obezite")

elif vki >=35 and vki < 40:
    print("2.Derece obezite")

else:
    print("3.Derece obezite")           