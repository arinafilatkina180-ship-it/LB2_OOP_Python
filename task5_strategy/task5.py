
# Базовий клас стратегії планування
class StudyStrategy:

    def create_plan(self, tasks):
        raise NotImplementedError(
            "Метод create_plan() потрібно реалізувати у дочірньому класі."
        )


# Стратегія збалансованого планування
class BalancedStrategy(StudyStrategy):

    def create_plan(self, tasks):
        return tasks.copy()


# Стратегія виконання складних завдань спочатку
class DifficultFirstStrategy(StudyStrategy):

    def create_plan(self, tasks):
        return sorted(tasks, key=lambda task: task["difficulty"], reverse=True)


# Стратегія планування за термінами виконання
class DeadlineStrategy(StudyStrategy):

    def create_plan(self, tasks):
        return sorted(tasks, key=lambda task: task["days_left"])
    
# Нова стратегія: спочатку найлегші завдання
class EasyTasksFirstStrategy(StudyStrategy):

    def create_plan(self, tasks):
        return sorted(tasks, key=lambda task: task["difficulty"])

# Клас планувальника навчання
class StudyPlanner:

    def __init__(self, strategy):
        self.strategy = strategy

    # Зміна стратегії планування
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Створення плану за обраною стратегією
    def create_study_plan(self, tasks):
        return self.strategy.create_plan(tasks)

# Список навчальних завдань
tasks = [
    {"name": "Вивчити Python", "difficulty": 3, "days_left": 5},
    {"name": "Виконати лабораторну", "difficulty": 5, "days_left": 2},
    {"name": "Підготувати презентацію", "difficulty": 2, "days_left": 1},
    {"name": "Повторити матеріал", "difficulty": 1, "days_left": 7}
]


# Створення планувальника
planner = StudyPlanner(BalancedStrategy())

# Допоміжна функція для виведення плану
def show_plan(title, plan):
    print("\n" + title)
    for task in plan:
        print(
            task["name"],
            "| Складність:", task["difficulty"],
            "| Днів до завершення:", task["days_left"]
        )


# Демонстрація збалансованої стратегії
show_plan("=== Збалансоване планування ===",
          planner.create_study_plan(tasks))

# Зміна на стратегію складних завдань
planner.set_strategy(DifficultFirstStrategy())
show_plan("=== Спочатку складні завдання ===",
          planner.create_study_plan(tasks))

# Зміна на стратегію термінів виконання
planner.set_strategy(DeadlineStrategy())
show_plan("=== Спочатку найближчі терміни ===",
          planner.create_study_plan(tasks))

# Демонстрація нової стратегії
planner.set_strategy(EasyTasksFirstStrategy())

show_plan("=== Спочатку найлегші завдання ===",
          planner.create_study_plan(tasks))
