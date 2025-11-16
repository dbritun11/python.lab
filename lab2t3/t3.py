text = input("Введите текст: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Словарь символов и их значения: ")
print(char_count)