"""
Домашнее задание №1
Функции и структуры данных
"""
my_list = [1, 6, 95, 69, 7, 24, 60]
my_list_1 = [1, 3, 27, 69, 7, 24, 60]


def power_numbers(*some_list):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [i ** 2 for i in some_list]


power_numbers(1, 6, 95, 69, 7, 24, 60)
print(power_numbers(1, 6, 95, 69, 7, 24, 60))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        pass
    return True


def filter_numbers(param, *some_list):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if param == ODD:
        return list(filter(lambda x: x % 2 != 0, some_list))
    if param == EVEN:
        return list(filter(lambda x: x % 2 == 0, some_list))
    if param == PRIME:
        return list(filter(is_prime, some_list))


print(filter_numbers(PRIME, 5, 6, 9))

