# Самостоятельная работа №1

# Задача №1. Куб
def make_cube(n):
    return n ** 3

# Задача №2. Повторение
def repeat(value):
    if isinstance(value, str):
        return value * 3
    return str(value) * 2

# Задача №3. Возведение в степень
def create_powers(*numbers, degree):
    return [number ** degree for number in numbers]

# Задача №4. Разворот числа
def reverse_number(number):
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number //= 10
    return result

# Задача №5*. Рекурсия (задача со звёздочкой)
def fac(number):
    if number == 1:
        return 1
    return fac(number - 1) * number

if __name__ == '__main__':
    print()
    print('make cube:')
    print('3:', make_cube(3))

    print('repeat:')
    print('str spam:', repeat('spam'))
    print('int 123:', repeat(123))

    print('create_powers:')
    print('degree:', create_powers(3, 4, 5, degree=3))
    print('reverse_number:')
    
    print('reverse:', reverse_number(556))
    print('reverse:', reverse_number(123456789))
    print('fac:')
    print(fac(5))
