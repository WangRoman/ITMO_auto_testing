class Soda:
    def __init__(self, addition=None):
        self.addition = addition
    def show_my_drink(self):
        if self.addition:
            print(f'Газировка и {self.addition}')
        else:
            print('Обычная газировка')
drink1 = Soda()
drink2 = Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()

class Mammal:
    className = 'Млекопитающее'
class Dog(Mammal):
    species = 'Canis Lupus'
dog = Dog()
print(dog.className)