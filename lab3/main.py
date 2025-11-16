class Library:

    libraries_quantity = 0

    def __init__(self):
        self.books = {}
        Library.libraries_quantity += 1

    def __del__(self):
        Library.libraries_quantity -= 1

    def add_book(self, title):
        self.books[title] = 1

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]

    def find_book(self, title):
        if title in self.books and self.books[title] == 1:
            return True
        return False

    def show_all_available_books(self):
        available_books = []
        for title, available in self.books.items():
            if available == 1:
                available_books.append(title)
        return available_books

    def __str__(self):
        return f"Library with {len(self.books)} books"

    def __repr__(self):
        return f"Library(books={self.books})"

lib = Library()

lib.add_book("Война и мир")
lib.add_book("Преступление и наказание")
lib.add_book("Евгений Онегин")
lib.add_book("Мастер и Маргарита")
lib.add_book("Анна Каренина")
lib.add_book("Джейн Эйр")
lib.add_book("Жестокий принц")

print("После добавления книг:")
print("Доступные книги:", lib.show_all_available_books())
print()

print("Есть ли 'Война и мир'?", lib.find_book("Война и мир"))
print("Есть ли 'Анна Каренина'?", lib.find_book("Анна Каренина"))
print("Есть ли 'Мёртвые души'?", lib.find_book("Мёртвые души"))
print()

lib.books["Анна Каренина"] = 0
print("После того как 'Анна Каренина' стала недоступной:")
print("Доступные книги:", lib.show_all_available_books())
print()

lib.remove_book("Жестокий принц")
print("После удаления 'Жестокий принц':")
print("Доступные книги:", lib.show_all_available_books())
print()

print("Количество библиотек:", Library.libraries_quantity)
