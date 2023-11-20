number_list = []

for i in range(1,11):
    sayi = int(input("Enter a number: "))
    number_list.append(sayi)
enbuyuk = number_list[0]
enkucuk = number_list[0]
for i in number_list:
    if i > enbuyuk:
        enbuyuk = i 
    elif i < enkucuk:
        enkucuk = i 
print(enbuyuk,enkucuk)    
