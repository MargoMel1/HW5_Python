''' Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.'''


def find_sum(max_num, cur_num=1, sum=0):
    if cur_num > max_num:
        return float(sum)
    sum += cur_num
    cur_num += 1
    return find_sum(max_num, cur_num, sum)


num = int(input('Введите число: '))
rec_sum = find_sum(num)
f_sum = num * (num + 1) / 2
if rec_sum == f_sum:
    print(f'{rec_sum} равно {f_sum}')
