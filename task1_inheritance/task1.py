# Базовий клас транспортного засобу
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        return "Транспортний засіб рухається."

    def __str__(self):
        return f"Марка: {self.brand}, швидкість: {self.speed} км/год"
    # Підклас автомобіля
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def move(self):
        return f"Автомобіль {self.brand} їде дорогою зі швидкістю {self.speed} км/год."

    def __str__(self):
        return super().__str__() + f", тип пального: {self.fuel_type}"
    # Підклас мотоцикла
class Motorcycle(Vehicle):
    def __init__(self, brand, speed, engine_volume):
        super().__init__(brand, speed)
        self.engine_volume = engine_volume

    def move(self):
        return f"Мотоцикл {self.brand} їде дорогою зі швидкістю {self.speed} км/год."

    def __str__(self):
        return super().__str__() + f", об'єм двигуна: {self.engine_volume} см³"
    # Підклас автобуса
class Bus(Vehicle):
    def __init__(self, brand, speed, passenger_capacity):
        super().__init__(brand, speed)
        self.passenger_capacity = passenger_capacity

    def move(self):
        return f"Автобус {self.brand} перевозить пасажирів зі швидкістю {self.speed} км/год."

    def __str__(self):
        return super().__str__() + f", кількість пасажирів: {self.passenger_capacity}"
    # Створення об'єктів різних класів
car = Car("Toyota", 180, "Бензин")
motorcycle = Motorcycle("Yamaha", 150, 600)
bus = Bus("Mercedes", 90, 50)

# Створення списку транспортних засобів
vehicles = [car, motorcycle, bus]

# Демонстрація поліморфізму
print("=== Поліморфізм ===")

for vehicle in vehicles:
    print(vehicle)
    print(vehicle.move())
    print()
    # Перевірка типів об'єктів
print("=== Перевірка типів ===")

print("car є об'єктом Car:", isinstance(car, Car))
print("car є об'єктом Vehicle:", isinstance(car, Vehicle))
print("motorcycle є об'єктом Bus:", isinstance(motorcycle, Bus))

# Перевірка спадковості класів
print("Car є підкласом Vehicle:", issubclass(Car, Vehicle))
print("Motorcycle є підкласом Vehicle:", issubclass(Motorcycle, Vehicle))
print("Bus є підкласом Vehicle:", issubclass(Bus, Vehicle))