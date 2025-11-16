sentence = input("Введите предложение: ")

words = sentence.split()

dict = {}

for word in words:
    dict[word] = len(word)

print("Словарь и длины: ")
print(dict)
