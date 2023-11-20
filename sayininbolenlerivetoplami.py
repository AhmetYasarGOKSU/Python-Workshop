number = int(input("Enter a number: "))
total = 0
list = []
for i in range(1,number // 2 + 1):
    if number % i == 0:
        list.append(i)
        total += i 
print(f"Divisors of the number: {list}")
print(f"Sum of divisors of the number: {total}")
