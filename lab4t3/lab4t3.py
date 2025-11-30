import numpy as np
import matplotlib.pyplot as plt

categories = ['Спорт', 'Музыка', 'Кино', 'Путешествия', 'Игры']
values = [20, 25, 15, 30, 10]  # количество пользователей или процентов

plt.figure(figsize=(8, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90,
        colors=['skyblue', 'lightgreen', 'salmon', 'gold', 'violet'])

plt.title('Предпочтения пользователей по категориям', fontsize=16)

plt.savefig('user_preferences_pie.png', dpi=300, bbox_inches='tight')
plt.show()
