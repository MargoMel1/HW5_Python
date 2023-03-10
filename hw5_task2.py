''' Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''


def calculate_even_and_odd_digits_of_number(number, even=0, odd=0):
    if number == 0:
        print(f'Количество чётных цифр: {even}')
        print(f'Количество нечётных цифр: {odd}')
        return
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number // 10
    calculate_even_and_odd_digits_of_number(number, even, odd)


number = int(input('Введите число: '))
calculate_even_and_odd_digits_of_number(number)
