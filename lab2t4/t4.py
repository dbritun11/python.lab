N = int(input("Введите число: "))

divisors = []

for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)

print("Количество делителей числа: ", len(divisors))