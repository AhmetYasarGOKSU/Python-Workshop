sayi_list = [5,20,34,15,39,2]
sonuc_list = []
for i in range(0, len(sayi_list)):
    carpim = 1
    for j in range(i+1, len(sayi_list)):
        carpim *= sayi_list[j]
    for k in range(0, i):
        carpim *= sayi_list[k]
    sonuc_list.append(carpim)
    #print(f"{i+1}.sayi haric sayilarin carpimi = {carpim}")
print(sonuc_list)