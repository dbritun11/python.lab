text = input("Введите строку: ")
vowels = "aeiouAEIOU"

result = ""
for char in text:
    if char not in vowels:
        result += char

print("Результат:", result)