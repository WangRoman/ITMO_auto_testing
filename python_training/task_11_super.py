class Parent:
    def __init__(self):
        print("Инициализация родительского класса")

    def greet(self):
        print("Привет из родительского класса")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Вызов метода __init__ родительского класса
        print("Инициализация дочернего класса")

    def greet(self):
        super().greet()  # Вызов метода greet родительского класса
        print("Привет из дочернего класса")

# Пример использования
child_instance = Child()
child_instance.greet()