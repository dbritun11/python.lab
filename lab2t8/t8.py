numbers = [10, 4, 9, 3, 6, 1]

average = sum(numbers)/len(numbers)

result = []

for num in numbers:
    if num <= average:
        result.append(num)

print("Среднее арифметическое: ", average)
print("Список с элементами больше сренего: ", result)