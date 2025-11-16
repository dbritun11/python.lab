num = int(input("Введите число: "))

if num % 7 == 0:
    print("Магическое число!")
else:
    digit_sum = sum(int(d) for d in str(num))
    print("Сумма цифр:", digit_sum)