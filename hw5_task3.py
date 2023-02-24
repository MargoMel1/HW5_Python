''' Задание 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321 '''


def recursion(number, result):
    if number == 0:
        return result
    ost = number % 10
    number //= 10
    result += str(ost)
    print(f'{number}  -  {result}')

    return recursion(number, result)


number = int(input('Введите число:'))
result = ''
result = recursion(number, result)
print(f'ответ {number} -> {result}')
