seconds = int(input("Введите количество секунд: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(f"{minutes} минута(ы) {remaining_seconds} секунд(ы)")