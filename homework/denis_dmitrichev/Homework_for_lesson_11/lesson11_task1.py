class Book:
    material = 'бумага'
    text = True

    def __init__(self, title, author, num_of_pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def book_info(self):
        if self.reserved:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.num_of_pages}, материал: {self.material}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.num_of_pages}, материал: {self.material}')


idiot = Book('Идиот', 'Достоевский', '599', '9780226159621', False)

the_lord_of_the_ring = Book('Властелин колец', 'Толкин',
                            '1005', '9788845292613', False)

queen_margot = Book('Королева Марго', 'Дюма', '640', '9788440653222', False)

orwell_1984 = Book('1984', 'Джордж Оруэлл', '320', '9789510459959', False)

suite = Book('Чемодан', 'Сергей Довлатов', '128', '9780802112460', False)


suite.reserved = True

books = [idiot, the_lord_of_the_ring, queen_margot, orwell_1984, suite]
for book in books:
    book.book_info()


class SchoolBook(Book):
    def __init__(self, subject, num_of_grade, title, author, num_of_pages, isbn, tasks=True, reserved=False):
        super().__init__(title, author, num_of_pages, isbn, reserved)
        self.subject = subject
        self.num_of_grade = num_of_grade
        self.tasks = tasks

    def book_info(self):
        if self.reserved:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.num_of_pages}, предмет: {self.subject},'
                  f' класс: {self.num_of_grade}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.num_of_pages}, предмет: {self.subject}, класс: {self.num_of_grade}')


math_5_grade = SchoolBook("Математика", 5,
                          "Математика. 5 класс", "Н.Я. Виленкин",
                          280, "978-5-09-079452-3", True, False)

russian_7_grade = SchoolBook("Русский язык", 7, "Русский язык. 7 класс",
                             "М.Т. Баранов", 223,
                             "978-5-09-079453-0", True, False)

history_9_grade = SchoolBook("История России", 9,
                             "История России. 9 класс", "А.А. Данилов",
                             303, "978-5-09-079454-7", False, False)

literature_10_grade = SchoolBook("Литература", 10,
                                 "Литература. 10 класс", "Ю.В. Лебедев",
                                 367, "978-5-09-079455-4", True, False)

physics_11_grade = SchoolBook("Физика", 11,
                              "Физика. 11 класс", "Г.Я. Мякишев",
                              399, "978-5-09-079456-1", True, False)


literature_10_grade.reserved = True

school_books = [math_5_grade, russian_7_grade, history_9_grade, literature_10_grade, physics_11_grade]
for book in school_books:
    book.book_info()
