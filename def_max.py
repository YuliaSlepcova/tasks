number = input()
def maximum(number: str):
    q = int(number[0])
    max = 0
    for a in range(len(number)):
        q = int(number[a])
        if max < q:
            max = q
    print(max)
maximum(number)
