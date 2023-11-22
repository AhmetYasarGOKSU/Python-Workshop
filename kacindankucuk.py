number = int(input("Enter a number: "))
number_list = [3,5,9,7,11,13,17,19,23,29,31,37,41,43,47,53]
x = 0 
for i in range(0,len(number_list)):
    if number < number_list[i]:
        x += 1
print(x)
