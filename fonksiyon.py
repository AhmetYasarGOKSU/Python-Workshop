def sayilarin_toplami(basla,bitir):
    toplam = 0      
    for i in range(basla,bitir+1):
        toplam += i 
    return toplam
tüm_toplam = sayilarin_toplami(3,15) + sayilarin_toplami(10,40) + sayilarin_toplami(15,70)
print(tüm_toplam)