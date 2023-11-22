result = 0
number = int(input("Enter a number: "))
def func(n):
    total = 1/n - 1/(n + 2)
    return total
for i in range(1,number+1,2):
    result += func(i)
print(result)
