number = int(input("Enter a number: "))
result = 0  
factorial_result = 1
def factorial(a):
    global factorial_result
    for i in range(1,a+1):
        factorial_result *= i
    return factorial_result
for i in range(1,number+1):
    result += i / factorial(i+1)
print(result)   
