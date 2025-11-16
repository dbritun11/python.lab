base_price = 24.99
included_minutes = 60
included_sms = 30
included_data_mb = 1024

extra_minute_price = 0.89
extra_sms_price = 0.59
extra_mb_price = 0.79
tax_rate = 0.02

used_minutes = int(input("Введите количество использованных минут: "))
used_sms = int(input("Введите количество отправленных SMS: "))
used_data_mb = int(input("Введите объем использованного интернет-трафика (в МБ): "))

extra_minutes = max(0, used_minutes - included_minutes)
extra_sms = max(0, used_sms - included_sms)
extra_data_mb = max(0, used_data_mb - included_data_mb)

extra_minutes_cost = extra_minutes * extra_minute_price
extra_sms_cost = extra_sms * extra_sms_price
extra_data_cost = extra_data_mb * extra_mb_price

subtotal = base_price + extra_minutes_cost + extra_sms_cost + extra_data_cost

tax = subtotal * tax_rate

total = subtotal + tax

print(f"\nБазовая стоимость тарифа: {base_price:.2f} руб.")

if extra_minutes > 0:
    print(f"Доп. минуты ({extra_minutes} мин): {extra_minutes_cost:.2f} руб.")
if extra_sms > 0:
    print(f"Доп. SMS ({extra_sms} шт): {extra_sms_cost:.2f} руб.")
if extra_data_mb > 0:
    print(f"Доп. интернет ({extra_data_mb} МБ): {extra_data_cost:.2f} руб.")

print(f"Налог (2%): {tax:.2f} руб.")
print(f"Итоговая сумма к оплате: {total:.2f} руб.")