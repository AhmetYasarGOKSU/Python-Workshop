list = [1,2,3,5,6,7]
eleman_sirasi = int(input("Kaçinci siraya eleman eklemek istiyorsunuz: "))
eleman = int(input("Hangi elemani eklemek istiyorsunuz: "))
list.append(eleman)
for i in range(eleman_sirasi - 1,len(list)):
    list[i], list[len(list)-1] = list[len(list)-1], list[i]
print(list)    