tc_no = (input("TC kimlik numaranizi girin: "))

def tekler_toplam(b):
    toplamt = 0 
    for i in range(0,10,2):
        toplamt += int(b[i])
    return toplamt
def ciftler_toplam(a):
    toplamc = 0 
    for i in range(1,9,2):
        toplamc += int(a[i])
    return toplamc    
def tüm_toplam(c):
    toplam = 0
    for i in range(0,10):
        toplam += int(c[i])
    return toplam
if tc_no[0] == "0":
    print("TC kimlik numaraniz gecersiz!")
elif (tekler_toplam(tc_no)*7 - ciftler_toplam(tc_no)) % 10 != int(tc_no[9]):
    print("TC kimlik numaraniz gecersiz!")
elif tüm_toplam(tc_no) % 10 != int(tc_no[10]):
    print("TC kimlik numaraniz gecersiz!")
else:
    print("TC kimlik numaraniz geçerli")
