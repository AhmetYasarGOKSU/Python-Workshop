number = int(input("Enter a number: "))
twosystem = ""
while number != 1:
    if number % 2 == 0:
        number //= 2
        twosystem = "0" + twosystem
    else:
        number //= 2     
        twosystem = "1" + twosystem
twosystem = "1" + twosystem
print(twosystem)


number = int(input("Enter a number: "))
twosystem = ""
while number != 0:
    twosystem = str(number % 2) + twosystem
    number //= 2
print(twosystem if twosystem else "0")
