''' Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ... Количество элементов (n) вводится с клавиатуры.'''


def find_sum(steps, cur_step=1, count=0.0, el_1=1.0):
    if cur_step > steps:
        print(count)
        return

    count += el_1
    el_1 /= -2
    cur_step += 1

    find_sum(steps, cur_step, count, el_1)


n = int(input('Введите количество слагаемых: '))
find_sum(n)
