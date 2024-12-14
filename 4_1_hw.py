#Задание 4
class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def starting(self):
        print("Автомобиль заведён")
    def turning_off(self):
        print("Автомобиль заглушён")
    def yearAppropriation(self):
        print(f'Автомобилю присвоен год: {self.year}')
    def typeAppropriation(self):
        print(f'Автомобилю присвоен тип: {self.type}')
    def colorAppropriation(self):
        print(f'Автомобилю присвоен цвет: {self.color}')

hyundai = Car("черный", "седан", "2020")
kia = Car("белый", "хэтчбэк", "2006")
honda = Car("темно-синий", "седан", "2021")
nissan = Car("красный", "внедорожник", "2022")
chevrolet = Car("голубой", "кроссовер", "2019")
hyundai.starting()
hyundai.turning_off()
hyundai.yearAppropriation()
hyundai.typeAppropriation()
hyundai.colorAppropriation()
kia.starting()
kia.turning_off()
kia.yearAppropriation()
kia.typeAppropriation()
kia.colorAppropriation()
honda.starting()
honda.turning_off()
honda.yearAppropriation()
honda.typeAppropriation()
honda.colorAppropriation()
nissan.starting()
nissan.turning_off()
nissan.yearAppropriation()
nissan.typeAppropriation()
nissan.colorAppropriation()
chevrolet.starting()
chevrolet.turning_off()
chevrolet.yearAppropriation()
chevrolet.typeAppropriation()
chevrolet.colorAppropriation()