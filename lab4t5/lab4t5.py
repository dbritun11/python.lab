import matplotlib.pyplot as plt

categories = ['Спорт', 'Музыка', 'Кино', 'Путешествия', 'Игры']
values = [25, 40, 30, 20, 15]

plt.figure(figsize=(8, 6))

plt.barh(categories, values, color=['skyblue', 'lightgreen', 'salmon', 'gold', 'violet'])

plt.xlabel('Количество пользователей', fontsize=12)
plt.ylabel('Категории', fontsize=12)
plt.title('Популярность категорий среди пользователей', fontsize=16)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.savefig('horizontal_bar.png', dpi=300, bbox_inches='tight')
plt.show()
