ilk_sayi = int(input("Araliğin ilk sayisini giriniz: "))
son_sayi = int(input("Araliğin son sayisini giriniz: "))
list = []
for i in range(ilk_sayi, son_sayi+1):
    if i % 3 == 0:
        list.append(i)
print(list)