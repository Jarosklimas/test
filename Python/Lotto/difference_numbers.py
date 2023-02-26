numbers = [1, 5, 9, 10, 20, 50]
result = numbers[0]

for i in range(1, len(numbers)):
    result -= numbers[i]

print(result)