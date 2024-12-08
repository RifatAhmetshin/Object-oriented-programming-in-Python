from task_1 import Dog, Car, Book# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":

    try:
        dog_invalid = Dog("Рекс", -1)  # Неверный возраст
    except ValueError:
        print("Ошибка: неправильные данные")


    try:
        car_invalid = Car("Ford", 1800)  # Неверный год
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        book_invalid = Book("Невыносимая легкость бытия", "Милан Кундера", -100)  # Неверное количество страниц
    except ValueError:
        print("Ошибка: неправильные данные")
