number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
common_divisor = []
divisor = 2 
ebob = 1 
while number1 > 1 and number2 > 1:
    if number1 % divisor == 0 and number2 % divisor == 0:
        common_divisor.append(divisor)
        ebob *= divisor
        number1 //= divisor
        number2 //= divisor 
    elif number1 % divisor == 0 and number2 % divisor != 0:
        number1 //= divisor
        divisor += 1
    elif number1 % divisor != 0 and number2 % divisor == 0:
        number2 //= divisor  
        divisor += 1
    elif number1 % divisor != 0 and number2 % divisor !=0:
        divisor += 1

print(common_divisor)
print(ebob)      

