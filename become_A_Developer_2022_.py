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
# with open('10m.txt', 'r', encoding = 'utf-8') as file:
#     f= file.readlines()
#     # int_seqence= map(lambda x: int(x), f)
#     int_seqence= list(map(lambda x: int(x), f))
#     np_arr = np.array(int_seqence)

# print(np.min(np_arr))
# print(np.max(np_arr))
# print(np.median(np_arr))
# print(np.sum(np_arr)/len(np_arr))
# print(np.mean(np_arr))

f = np.loadtxt('10m.txt')

print(np.min(f))
print(np.max(f))
print(np.median(f))
print(np.sum(f)/len(f))
print(np.mean(f))
