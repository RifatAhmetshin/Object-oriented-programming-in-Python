# TODO: Подробно описать три произвольных класса


class Dog:
    def __init__(self, name: str, age: int):
        """
        Инициализация объекта "Собака".

        :param name: Имя собаки.
        :param age: Возраст собаки. Не может быть отрицательным.

        :raises ValueError: Если возраст собаки меньше 0.

        Примеры:
        >>> dog = Dog("Бобик", 3)
        >>> dog.name
        'Бобик'
        >>> dog.age
        3
        >>> dog.bark()
        'Бобик говорит: Гав!'
        """
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name = name
        self.age = age

    def bark(self) -> str:
        """
        Лай собаки.

        :return: Строка с лаем собаки.

        Примеры:
        >>> dog = Dog("Бобик", 3)
        >>> dog.bark()
        'Бобик говорит: Гав!'
        """
        return f"{self.name} говорит: Гав!"

    def birthday(self) -> None:
        """
        День рождения собаки, увеличиваем возраст на 1.

        Примеры:
        >>> dog = Dog("Бобик", 3)
        >>> dog.birthday()
        >>> dog.age
        4
        """
        self.age += 1


if __name__ == "__main__":
    doctest.testmod()



import doctest


class Car:
    def __init__(self, model: str, year: int):
        """
        Инициализация объекта "Машина".

        :param model: Модель машины.
        :param year: Год выпуска машины. Должен быть не меньше 1886.

        :raises ValueError: Если год выпуска машины меньше 1886.

        Примеры:
        >>> car = Car("Toyota", 2020)
        >>> car.model
        'Toyota'
        >>> car.year
        2020
        >>> car.drive()
        'Машина Toyota едет.'
        """
        if year < 1886:
            raise ValueError("Неверный год выпуска машины.")
        self.model = model
        self.year = year

    def drive(self) -> str:
        """
        Машина едет.

        :return: Строка, что машина едет.

        Примеры:
        >>> car = Car("Toyota", 2020)
        >>> car.drive()
        'Машина Toyota едет.'
        """
        return f"Машина {self.model} едет."

    def get_age(self) -> int:
        """
        Возвращает возраст машины.

        :return: Возраст машины.

        Примеры:
        >>> car = Car("Toyota", 2020)
        >>> car.get_age()
        4
        """
        return 2024 - self.year


if __name__ == "__main__":
    doctest.testmod()


import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта "Книга".

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц книги. Должно быть больше 0.

        :raises ValueError: Если количество страниц <= 0.

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.title
        '1984'
        >>> book.author
        'Джордж Оруэлл'
        >>> book.read()
        "Читаем книгу '1984'."
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self) -> str:
        """
        Чтение книги.

        :return: Строка с информацией о том, что книга читается.

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.read()
        "Читаем книгу '1984'."
        """
        return f"Читаем книгу '{self.title}'."

    def get_info(self) -> str:
        """
        Получить информацию о книге.

        :return: Строка с названием, автором и количеством страниц книги.

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.get_info()
        "'1984' написана Джордж Оруэлл, имеет 328 страниц."
        """
        return f"'{self.title}' написана {self.author}, имеет {self.pages} страниц."


if __name__ == "__main__":
    doctest.testmod()


