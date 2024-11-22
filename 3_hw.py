#Задача 2
def numbers(a: int = 3, b: int = 5) -> int:
    return max(3, 5)
print(numbers())

#Задача 3
def numbers1(c, d):
    if c - d == 135 or d - c == 135:
        print('yes')
    else:
        print('No')

numbers1(10, 145)

#Задача 4
def season(month):
    if month == 1 or month == 2 or month == 12:
        print("зима")
    elif month in range(3, 6):
        print("весна")
    elif 6 <= month <= 8:
        print("лето")
    elif month in range(9, 12):
        print("осень")
    else:
        print("Введите корректный номер месяца")

season(7)

#Задача 5
def numbers2(e, f, g):
    if e > 10 and f > 10 and g > 10:
        print('yes')
    else:
        print('no')

numbers2(7, 12, 18)

#Задача 6
def numbers3(list):
    count = 0
    for elem in list:
        if elem >= 0:
            count += 1
    print("Всего положительных чисел: " + str(count))
numbers3([2, -1, 3, -5, 4])

#Задача 7
def days_quantity(years, months) -> int:
    years_days = years * 348
    months_days = months * 29
    days = years_days + months_days
    print(days)
days_quantity(5, 7)


