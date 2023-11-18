ayrilacak_cumle = input("Bir cümle giriniz: ")
kelime = ""
for i in range(len(ayrilacak_cumle)):
    kelime += ayrilacak_cumle[i]
    if ayrilacak_cumle[i] == " " or i == len(ayrilacak_cumle) - 1:
        print(kelime)
        kelime = ""
