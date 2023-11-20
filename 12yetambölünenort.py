total = 0 
divisor_number = 0 
for i in range(1,1001):
    if i % 12 == 0:
        total += i
        divisor_number += 1
Average = total / divisor_number
print(Average)