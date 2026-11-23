# Клас профілю студента
class StudentProfile:
    def __init__(self, name, faculty, grade, completed_tasks, total_tasks):
        self.name = name
        self._faculty = faculty
        self.__grade = grade
        self.completed_tasks = completed_tasks
        self.total_tasks = total_tasks

    # Getter для приватного атрибута grade
    @property
    def grade(self):
        return self.__grade

    # Setter з перевіркою значення оцінки
    @grade.setter
    def grade(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Оцінка повинна бути числом.")

        if not 0 <= value <= 100:
            raise ValueError("Оцінка повинна бути в діапазоні від 0 до 100.")

        self.__grade = value

    # Обчислювана властивість прогресу виконання завдань
    @property
    def progress(self):
        if self.total_tasks <= 0:
            return 0

        return (self.completed_tasks / self.total_tasks) * 100
    # Створення об'єкта профілю студента
student = StudentProfile("Аріна", "Кібербезпека", 90, 8, 10)

print("=== Профіль студента ===")
print("Ім'я:", student.name)
print("Факультет:", student._faculty)
print("Поточна оцінка:", student.grade)

# Перевірка setter
print("\n=== Зміна оцінки ===")
student.grade = 95
print("Нова оцінка:", student.grade)

# Перевірка обчислюваної властивості
print("\n=== Прогрес виконання завдань ===")
print("Виконано завдань:", student.completed_tasks)
print("Загальна кількість:", student.total_tasks)
print("Прогрес:", student.progress, "%")

# Зміна кількості виконаних завдань
student.completed_tasks = 9
print("Прогрес після виконання ще одного завдання:", student.progress, "%")

# Перевірка обробки некоректних значень
print("\n=== Перевірка помилкових значень ===")

try:
    student.grade = "високий"
except TypeError as error:
    print("TypeError:", error)

try:
    student.grade = -10
except ValueError as error:
    print("ValueError:", error)

try:
    student.grade = 120
except ValueError as error:
    print("ValueError:", error)

# Спроба прямого доступу до приватного атрибута
print("\n=== Приватний атрибут ===")

try:
    print(student.__grade)
except AttributeError as error:
    print("Прямий доступ заборонено:", error)

# Доступ до атрибута через name mangling
print("Доступ через name mangling:", student._StudentProfile__grade)