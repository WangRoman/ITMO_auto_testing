#Задача 1
def task_1() -> None:
    var_int: int = 42
    var_float: float = 3.14
    var_str: str = "Hello, World!"
    var_list: list = [1, 2, 3, 4, 5]
    var_bool: bool = True

    print(f'Type of var_int: {type(var_int)}')
    print(f'Type of var_float: {type(var_float)}')
    print(f'Type of var_str: {type(var_str)}')
    print(f'Type of var_list: {type(var_list)}')
    print(f'Type of var_bool: {type(var_bool)}')

task_1()

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
