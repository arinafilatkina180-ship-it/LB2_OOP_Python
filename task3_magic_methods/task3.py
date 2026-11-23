
# Клас двовимірного вектора
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Текстове представлення об'єкта
    def __str__(self):
        return f"Вектор({self.x}, {self.y})"

    # Представлення об'єкта для розробника
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # Додавання двох векторів
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Віднімання двох векторів
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # Множення вектора на число
    def __mul__(self, number):
        return Vector2D(self.x * number, self.y * number)

    # Порівняння векторів за координатами
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Порівняння векторів за довжиною
    def __lt__(self, other):
        return abs(self) < abs(other)

    # Кількість координат вектора
    def __len__(self):
        return 2

    # Обчислення довжини вектора
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# Створення об'єктів
vector1 = Vector2D(3, 4)
vector2 = Vector2D(1, 2)

# Демонстрація магічних методів
print("=== Представлення об'єктів ===")
print(vector1)
print(repr(vector1))

print("\n=== Арифметичні операції ===")
print("Додавання:", vector1 + vector2)
print("Віднімання:", vector1 - vector2)
print("Множення на число:", vector1 * 2)

print("\n=== Порівняння векторів ===")
print("Вектори рівні:", vector1 == vector2)
print("Перший вектор коротший:", vector1 < vector2)

print("\n=== Додаткові методи ===")
print("Кількість координат:", len(vector1))
print("Довжина першого вектора:", abs(vector1))
