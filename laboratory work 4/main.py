import doctest


class Vehicle:

    def __init__(self, model: str, year: int):
        """
        Создание и подготовка к работе объекта базового класса "Автомобили"

        :param model: Модель автомобиля
        :param year: Год выпуска

        Примеры:
        >>> vehicle = Vehicle("Mazda CX5", 2023)  # инициализация экземпляра класса
        """

        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """
        Метод, который запускает двигатель автомобиля

        Примеры:
        >>> vehicle = Vehicle("Mazda CX5", 2023)
        >>> vehicle.start_engine()
        """
        ...

    def accelerate(self, speed: int) -> None:
        """
        Метод, который разгоняет автомобиль до заданной скорости.

        :param speed(int): Скорость до которой необходимо разогнаться

        Примеры:
        >>> vehicle = Vehicle("Mazda CX5", 2023)
        >>> vehicle.accelerate(125)
        """
        ...

    def __str__(self):
        return f"{self.year} {self.model}"

    def __repr__(self):
        return f"Vehicle(model='{self.model}', year={self.year})"


class SportCar(Vehicle):
    def __init__(self, model: str, year: int, max_time_speed: float):
        """
        Создание и подготовка к работе объекта дочернего класса "Спортивные автомобили" от родительского "Автомобили"

        :param model: Модель автомобиля
        :param year: Год выпуска
        :param max_time_speed: Время разгона до 100 км/ч

        Примеры:
        >>> car = SportCar("Ford mustang", 2023, 2.6)  # инициализация экземпляра класса
        """
        super().__init__(model, year)
        self.max_time_speed = max_time_speed

    def start_engine(self) -> None:
        """
        Метод, который запускает двигатель автомобиля
        Унаследован от базового класса

        Примеры:
        >>> car = SportCar("Ford mustang", 2023, 2.6)
        >>> car.start_engine()
        """
        super().start_engine()

    def accelerate(self, speed: int) -> float:
        """
        Метод, который разгоняет автомобиль до заданной скорости.
        Расширен от метода родительского класса, так как для спорт-каров указывается еще время разгона

        :param speed(int): Скорость до которой необходимо разогнаться

        :return: Время, затраченное на разгон до указанной скорости

        Примеры:
        >>> car = SportCar("Ford mustang", 2023, 2.6)
        >>> car.accelerate(350)
        """
        super().accelerate(350)
        ...

    def __repr__(self):
        return f"Car(model='{self.model}', year={self.year}, max_time_speed={self.max_time_speed})"


if __name__ == "__main__":
    doctest.testmod()
