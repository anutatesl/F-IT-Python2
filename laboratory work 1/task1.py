import doctest
from typing import Union


# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    def __init__(self, model: str, tank_capacity: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Машина"

        :param model: Модель автомобиля
        :param tank_capacity: Объем бака автомобиля
        :param occupied_volume: Объем заполненной части бака

        Примеры:
        >>> car = Car("Mazda CX5", 58, 43)  # инициализация экземпляра класса
        """
        self.model = model

        if not isinstance(tank_capacity, (int, float)):
            raise TypeError("Объем бака должен быть типа int или float")
        if tank_capacity <= 0:
            raise ValueError("Объем бака должен быть положительным числом")
        self.tank_capacity = tank_capacity

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем заполненной части бака должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Объем заполненной части бака не может быть отрицательным числом")
        if occupied_volume > tank_capacity:
            raise ValueError("Объем заполненной части бака не может быть больше общего объема бака")
        self.occupied_volume = occupied_volume

    def check_tank(self) -> bool:
        """
        Метод, который проверяет, заполнен ли бак на 15% и больше

        :return: Надо заправляться или нет

        Примеры:
        >>> car = Car("Mazda CX5", 58, 43)
        >>> car.check_tank()
        """
        ...

    def refuel_the_car(self, petrol: Union[int, float]) -> None:
        """
        Метод, который заправляет машину

        :param petrol: Кол-во бензина в литрах, которые водитель хочет долить
        :raise ValueError: Если количество бензина превышает свободное место в баке, то вызываем ошибку

        Примеры:
        >>> car = Car("Mazda CX5", 58, 10)
        >>> car.refuel_the_car(40)
        """
        if not isinstance(petrol, (int, float)):
            raise TypeError("Добавляемый бензин должен быть типа int или float")
        if petrol < 0:
            raise ValueError("Добавляемый бензин должен быть положительным числом")
        ...


class ShootingGallery:
    def __init__(self, price: int, total_shots: int):
        """
        Создание и подготовка к работе объекта "Игровой Тир"

        :param price: Стоимость одной игры (руб.)
        :param total_shots: Общее число возможных выстрелов

        Примеры:
        >>> game = ShootingGallery(250, 15)  # инициализация экземпляра класса
        """
        if not isinstance(price, int):
            raise TypeError("Стоимость игры должна быть типа int")
        if price <= 0:
            raise ValueError("Стоимость игры должна быть положительным числом")
        self.price = price

        if not isinstance(total_shots, int):
            raise TypeError("Общее число возможных выстрелов должно быть типа int")
        if total_shots <= 0:
            raise ValueError("Общее число возможных выстрелов должно быть положительным числом")
        self.total_shots = total_shots

        self.lucky_shot = 0

    def pay_for_the_game(self, money: int) -> bool:
        """
        Метод, который проверяет, хватает ли у посетителя денег на оплату игры

        :param money: Деньги, которые есть у посетителя

        :return: Оплатил посетитель игру или нет

        Примеры:
        >>> game = ShootingGallery(250, 15)
        >>> game.pay_for_the_game(275)
        """
        if not isinstance(money, int):
            raise TypeError("Деньги должны быть типа int")
        ...

    def make_shots(self) -> None:
        """
        Метод, в котором происходит необходимое число выстрелов и подсчитываются попадания

        Примеры:
        >>> game = ShootingGallery(250, 15)
        >>> game.make_shots()
        """
        ...

    def is_win(self) -> bool:
        """
        Метод, который проверяет, было ли 90% и больше попаданий по мешеням

        :return: Выиграл посетитель или нет

        Примеры:
        >>> game = ShootingGallery(250, 15)
        >>> game.is_win()
        """
        ...


class Robot:
    def __init__(self, name: str, owner_name: str):
        """
        Создание и подготовка к работе объекта "Робот"

        :param name: Имя робота
        :param owner_name: Имя владельца робота

        Примеры:
        >>> robot = Robot("Louis", "Anna")  # инициализация экземпляра класса
        """

        self.name = name
        self.owner_name = owner_name

    def say_hello(self) -> None:
        """
        Метод, в котором робот здоровается со своим владельцем

        Примеры:
        >>> robot = Robot("Louis", "Anna")
        >>> robot.say_hello()
        """
        ...

    def say_bye(self) -> None:
        """
        Метод, в котором робот прощается со своим владельцем

        Примеры:
        >>> robot = Robot("Louis", "Anna")
        >>> robot.say_bye()
        """
        ...

    def say_smth(self, words: str) -> None:
        """
        Метод, в котором робот что-то говорит
        :param words: Слова, которые должен сказать робот

        Примеры:
        >>> robot = Robot("Louis", "Anna")
        >>> robot.say_smth("How are you?")
        """
        if not isinstance(words, str):
            raise TypeError("Слова должны быть типа str")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
