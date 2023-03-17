def is_armstrong(num):
    n = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    return num == sum

# Main program
lst = list(map(int, input("Enter the list of numbers: ").split()))

for i in range(len(lst)):
    if is_armstrong(lst[i]):
        lst[i] = 1
    else:
        lst[i] = 0

print(lst)
