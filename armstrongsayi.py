number = (input("Enter a number: "))
step = len(number)
total = 0
for i in range(0,step):
    total += int(number[i]) ** 3
    
if total == int(number):
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")    
