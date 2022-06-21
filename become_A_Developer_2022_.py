import numpy as np

"""
Завдання - знайти наступні чотири/шість значень:
    1. максимальне число в файлі;
    2. мінімальне число в файлі;
    3. медіану ( https://goo.gl/hiCwVw );
    4. середнє арифметичне значення ( https://goo.gl/XJeAjZ );
    5*. найбільшу послідовність чисел (які ідуть один за одним), яка збільшується (опціонально)
    6*. найбільшу послідовність чисел (які ідуть один за одним), яка зменьшується (опціонально)

"""

def mediana(int_seqence):
    if len(int_seqence)%2 == 0:
        return (int_seqence[(len(int_seqence)/2)-1]+int_seqence[len(int_seqence)/2])/2
    else:
        # i=round(int(len(int_seqence)/2,0))
        i=len(int_seqence)//2 + 1
        return int_seqence [i]


# ---------------
def decrease_sequence(int_seqence):
    help_char = []
    main_arr = []
    for char in int_seqence:
        if len(help_char) == 0 or char < help_char[len(help_char) - 1]:
            help_char.append(char)
        else:
            main_arr.append(help_char)
            help_char = []
    return len(sorted(main_arr, key=lambda x: len(x))[-1])


# ---------
def increase_sequence(int_seqence):
    help_char = []
    main_arr = []
    for char in int_seqence:
        if len(help_char) == 0 or char > help_char[len(help_char) - 1]:
            help_char.append(char)
        else:
            main_arr.append(help_char)
            help_char = []
    # print('Найбільша зростаюча послідовність', len(sorted(main_arr, key=lambda x: len(x))[-1]))
    return len(sorted(main_arr, key=lambda x: len(x))[-1])


# ------ first way____________
print('First_way')
if __name__ == "__main__":

    with open('10m.txt', 'r', encoding = 'utf-8') as file:
        f= file.readlines()
        int_seqence= list(map(lambda x: int(x), f))
    print(' максимальне число в файлі = ', max(int_seqence))
    print(' мінімальне число в файлі = ', min(int_seqence))
    print(' медіана = ', mediana(int_seqence))
    print(' середнє арифметичне значення = ', sum(int_seqence)/len(int_seqence))
    print(' найбільша послідовність чисел (які ідуть один за одним), яка збільшується (опціонально) = ', increase_sequence(int_seqence))
    print(' найбільша послідовність чисел (які ідуть один за одним), яка зменьшується (опціонально) = ', decrease_sequence(int_seqence))

# ---------------------second_way-------------------------
print('Second_way')
f = np.loadtxt('10m.txt')
print(' максимальне число в файлі = ', np.max(f))
print(' мінімальне число в файлі = ', np.min(f))
print(' медіана = ', mediana(f))
print(' середнє арифметичне значення = ', np.mean(f))
print(' найбільша послідовність чисел (які ідуть один за одним), яка збільшується (опціонально) = ', increase_sequence(f))
print(' найбільша послідовність чисел (які ідуть один за одним), яка зменьшується (опціонально) = ', decrease_sequence(f))




