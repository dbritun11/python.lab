ip = input("Введите IP-адрес: ")

parts = ip.split(".")

if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
    print("Корректный IP-адрес")
else:
    print("Некорректный IP-адрес")