num_float = 3.4

if num_float > 0:
    print('positive number')
elif num_float == 0:
    print('zero')
else:
    print('Negative number')

permit_print = True
num = 3

if num > 0 and permit_print:
    print('num - positive number')
elif not permit_print:
    print('Print is forbidden')

def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print("You're a bachelor")
    elif year_of_study in range(5, 7):
        print("You're a master")
    elif 7 <= year_of_study <= 9:
        print("You're a graduate student")
    else:
        print("Input correct year of studing")

student_rank(5)

def number(numb):
    if -100 <= numb <= 100:
        print('-')
    else:
        print('+')

number(101)
