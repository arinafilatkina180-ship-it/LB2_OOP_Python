
from abc import ABC, abstractmethod


# Абстрактний клас способу доставки
class DeliveryMethod(ABC):

    @property
    @abstractmethod
    def delivery_name(self):
        pass

    @abstractmethod
    def calculate_cost(self, distance):
        pass

    @abstractmethod
    def deliver(self, order):
        pass

    # Звичайний метод абстрактного класу
    def show_information(self):
        return f"Спосіб доставки: {self.delivery_name}"


# Клас кур'єрської доставки
class CourierDelivery(DeliveryMethod):

    @property
    def delivery_name(self):
        return "Кур'єрська доставка"

    def calculate_cost(self, distance):
        return distance * 15

    def deliver(self, order):
        return f"Замовлення «{order}» доставляє кур'єр."


# Клас поштової доставки
class PostalDelivery(DeliveryMethod):

    @property
    def delivery_name(self):
        return "Поштова доставка"

    def calculate_cost(self, distance):
        return distance * 8

    def deliver(self, order):
        return f"Замовлення «{order}» відправлено поштою."


# Клас системи доставки (композиція)
class DeliveryService:

    def __init__(self, delivery_method):
        self.delivery_method = delivery_method

    def process_order(self, order, distance):
        print(self.delivery_method.show_information())
        print(self.delivery_method.deliver(order))
        print("Вартість доставки:", self.delivery_method.calculate_cost(distance), "грн")


# Демонстрація роботи програми
print("=== Кур'єрська доставка ===")
courier = CourierDelivery()
courier_service = DeliveryService(courier)
courier_service.process_order("Ноутбук", 10)

print("\n=== Поштова доставка ===")
postal = PostalDelivery()
postal_service = DeliveryService(postal)
postal_service.process_order("Книга", 10)


# Перевірка абстрактного класу
print("\n=== Перевірка абстрактного класу ===")

try:
    delivery = DeliveryMethod()
except TypeError as error:
    print("Помилка створення абстрактного класу:", error)
