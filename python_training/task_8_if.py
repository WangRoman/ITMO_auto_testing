num = 3

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число положительное')

str_1 = 'test'
str_2 = 'test1'

if str_2 == str_1:
    print('да')
else:
    print('нет')

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('yes')
    else:
        print('no')

task_yes_no(str_1 = 'test', str_2 = 'test1')