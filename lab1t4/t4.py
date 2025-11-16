amount = int(input("Введите сумму в рублях: "))

bills = [100, 50, 10, 5, 2, 1]

change = {}

for bill in bills:
    change[bill] = amount // bill
    amount %= bill

for bill in bills:
    print(f"{bill} руб: {change[bill]}")