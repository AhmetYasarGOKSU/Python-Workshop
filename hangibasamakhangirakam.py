number = (input("Enter a number: "))
queue = int(input("You want to know the number at which step(ones place is first): "))
step_number = len(number)-queue
if queue > len(number)-1:
    print("Your number is not long enough")
elif queue < 1:
    print("Step is not found")
else:
    print(number[step_number])    
