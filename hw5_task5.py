''' Задание 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке. '''

import string


def recursion(number, value):
    if number > value:
        return
    print(f'{number} {chr(number)}', end='\n')
    number += 1
    recursion(number, value)


n = 32
v = 127
recursion(n, v)
