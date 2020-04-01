number1, number2, number3 = int(input()), int(input()), int(input())
sum = number1 + number2 + number3
min = 0
max = 0
intermediate = 0
if number1 >= number2:
    max = number1
    min = number2
else:
    max = number2
    min = number1
if max <= number3:
    max = number3
if min >= number3:
    min = number3
intermediate = sum - max - min
print(max,min,intermediate, sep='\n')
