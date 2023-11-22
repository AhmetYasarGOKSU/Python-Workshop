sayi = int(input("Sayi: "))
for i in range(1, sayi+1):
    for j in range(1, i+1):
        if i ** 2 + j ** 2 == sayi:
            print(f"sayiniz {i} ve {j} nin kareleri toplamına eşittir.")
            continue
        else:
            continue