haftanin_günleri = ["Pazartesi", "Sali", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
gecen_gün = int(input("Kaç gün sonrasini öğrenmek istiyorsunuz: "))
bugün = input("Bugün hangi gün: ")
for i in range(0,7):
    if haftanin_günleri[i] == bugün:
        bugün_no = i
istenen_gün = bugün_no + gecen_gün
istenen_gün = istenen_gün % 7 
print(haftanin_günleri[istenen_gün])
        