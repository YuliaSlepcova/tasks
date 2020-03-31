number = int(input())
degree = 0
while 2**degree <= number:
    if number == 2**degree:
        break
    degree += 1
if number == 2**degree:
    print("yes")
else:
    print("no")
