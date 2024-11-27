#Задача 1
def task_1(a: int, b: float, c: str, d: list, e: bool) -> int:
    print("int, float, str, list, bool")
    return a, b, c, d, e
print(type(task_1(1, 2.5, 'three', [4, 5, 6], True)))
print()

#Задача 2
a = [1, 2, 3, 5, 8, 13, 21]
def task_2(a: list) -> int:
    return a[0:3]
print(task_2(a))
print()
#d. эта последовательность чисел называется списком

#Задача 3
def task_3(a: int = 5) -> int:
    return a**2
print(task_3())
