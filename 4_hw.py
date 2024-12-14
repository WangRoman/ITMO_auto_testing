#Задание 1
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def square(self):
        print(self.length * self.width)
    def perimeter(self):
        print(2 * (self.length + self.width))

obj1 = Rectangle(3, 5)
obj2 = Rectangle(2, 7)
obj3 = Rectangle(4, 9)
obj1.square()
obj1.perimeter()
obj2.square()
obj2.perimeter()
obj3.square()
obj3.perimeter()

#Задание 2
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        print(self.a + self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)
    def subtraction(self):
        print(self.a - self.b)

obj = Math(6, 2)
obj.addition()
obj.multiplication()
obj.division()
obj.subtraction()

#Задание 3
class Sidebar:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc
    def click(self):
        print(f"Клик по кнопке {self.text}")

button1 = Sidebar('Text Box', 'button', None)
button2 = Sidebar('Check Box', 'button', None)
button3 = Sidebar('Radio Button', 'button', None)
button4 = Sidebar('Web Tables', 'button', None)
button5 = Sidebar('Buttons', 'button', None)
button6 = Sidebar('Links', 'button', None)
button7 = Sidebar('Broken Links - Images', 'button', None)
button8 = Sidebar('Upload and Download', 'button', None)
button9 = Sidebar('Dynamic Properties', 'button', None)
button1.click()
button2.click()
button3.click()
button4.click()
button5.click()
button6.click()
button7.click()
button8.click()
button9.click()



