#fibonacci_basamak = int(input("Fibonaccinin kaç basamagini öğrenmek istiyorsunuz: "))
#fibonacci_ilk, fibonacci_son = 0, 1
#for i in range(fibonacci_basamak):
    #print(fibonacci_ilk)
    #    fibonacci_ilk, fibonacci_son = fibonacci_son, fibonacci_ilk + fibonacci_son

fibonacci_basamak = int(input("Fibonaccinin kaç basamagini öğrenmek istiyorsunuz: "))
fibonacci_ilk, fibonacci_orta = 1, 1
for i in range(0,fibonacci_basamak):
    if i <= 1:
        print(1)
    else:
        fibonacci_son = fibonacci_orta + fibonacci_ilk
        print(fibonacci_son)   
        fibonacci_ilk, fibonacci_orta = fibonacci_orta, fibonacci_son
