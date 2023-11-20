operatör = input("Which would you like to use operatör(‘+’, ‘-’, ‘x’, ‘/’): ")
number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
total = 0 
def ope(a):
    global operatör, number1, number2, total
    if a == "+":
        total = number1 + number2
    elif a == "-":
        total = number1 - number2
    elif a == "x":
        total = number1 * number2
    elif a == "/":
        total = number1 / number2
    print(total)
ope(operatör)

    