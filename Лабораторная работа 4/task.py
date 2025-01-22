class ElectronicDevice:

    def __init__(self, brand: str, model: str, power: int):
        self._brand = brand  # Инкапсуляция, чтобы предотвратить прямое изменение бренда.
        self.model = model
        self.power = power

    def __str__(self) -> str:
        return f"{self._brand} {self.model} ({self.power}W)"

    def __repr__(self) -> str:
        return f"ElectronicDevice(brand={self._brand}, model={self.model}, power={self.power})"

    def turn_on(self) -> str:
        """Включить устройство."""
        return f"{self._brand} {self.model} is now ON."

    def turn_off(self) -> str:
        """Выключить устройство."""
        return f"{self._brand} {self.model} is now OFF."


class Smartphone(ElectronicDevice):

    def __init__(self, brand: str, model: str, power: int, os: str, battery_capacity: int):
        super().__init__(brand, model, power)
        self.os = os
        self.battery_capacity = battery_capacity

    def __str__(self) -> str:
        return f"{self._brand} {self.model} ({self.os}, {self.battery_capacity}mAh)"

    def charge(self) -> str:
        """Зарядка устройства."""
        return f"{self._brand} {self.model} is charging."


class Laptop(ElectronicDevice):

    def __init__(self, brand: str, model: str, power: int, screen_size: float, is_touchscreen: bool):
        super().__init__(brand, model, power)
        self.screen_size = screen_size
        self.is_touchscreen = is_touchscreen

    def __str__(self) -> str:
        return f"{self._brand} {self.model} ({self.screen_size}-inch, Touchscreen: {self.is_touchscreen})"

    def turn_on(self) -> str:
        """
        Переопределение метода включения устройства.
        Причина: у ноутбуков процесс включения может включать загрузку операционной системы.
        """
        return f"{self._brand} {self.model} is booting up..."


if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 20, "iOS", 3200)
    laptop = Laptop("Dell", "XPS 13", 65, 13.4, True)

    print(phone)
    print(phone.charge())

    print(laptop)
    print(laptop.turn_on())
