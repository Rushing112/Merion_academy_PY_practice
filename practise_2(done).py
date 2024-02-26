# Самостоятельная работа №2

# Задача №1. Конвертация верблюда в змею

def camel_case_to_snake_case(line: str) -> str:
    result = []
    for idx, char in enumerate(line):
        if char.isupper() and idx:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)

# Задача №2. Повторение

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# Задача №3. Неабстрактные формы
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Задача №4. Ошибка суммы
class SecretResultReached(ValueError):
    pass

def add(x, y):
    total = x + y
    if total == 42:
        raise SecretResultReached('Secrat result was reached')
    return total




# Задача №5*. Габариты экрана

class Screen:
    def __init__(self, diagonal_inches, horizontal_pixels, vertical_pixels):
        self.diagonal_inches = diagonal_inches
        self.horizontal_pixels = horizontal_pixels
        self.vertical_pixels = vertical_pixels
        self.cm_in_inch = 2.54

    @property
    def aspect_ratio(self):
        return self.vertical_pixels / self.horizontal_pixels

    @property
    def height(self):
        return self.diagonal_inches / ((self.aspect_ratio ** 2 + 1)) ** 0.5

    @property
    def width(self):
        return self.aspect_ratio * self.height

    @property
    def height_cm(self):
        return self.height * self.cm_in_inch

    @property
    def width_cm(self):
        return self.width * self.cm_in_inch

    @property
    def area(self):
        return self.width * self.height

    @property
    def area_cm(self):
        return self.width_cm * self.height_cm


# Задача №6*. Валидные скобки
pairs =  {
    '{': '}',
    '[': "]",
    '(': ')',
}

def valid_parentheses(chars: str):
    stack = []
    for char in chars:
        if char in pairs:
            stack.append(char)
        else:
            if not (
                stack and
                pairs[stack.pop()] == char
            ):
                return False

    return not stack

if __name__ == '__main__':
    print('N1')
    print('camel_case_to_snake_case')
    print("'' ->", repr(camel_case_to_snake_case('')))
    print('Person.__name__ ->', camel_case_to_snake_case(Person.__name__))
    print('SuperUser ->', camel_case_to_snake_case('SomeCustomName'))
    print('SomeCustomName ->', camel_case_to_snake_case('SomeCustomName'))
    print('anotherCamelCase ->', camel_case_to_snake_case('anotherCamelCase'))
    print()
    print('№2')
    print('Person')
    person = Person('John', 'Smith')
    print(person.full_name)
    print()
    print('№3')
    rectangle = Rectangle(5,10)
    print('Rectangle Area:', rectangle.area())
    print('Rectangle Perimeter:', rectangle.perimeter())

    circle = Circle(5)
    print('Circle Area:', circle.area())
    print('Circle Perimeter', circle.perimeter())

    print()
    print('№4')
    print('secret sum value')
    print('1 + 2 =', add(1, 2))
    print('5 + 7 =', add(5, 7))
    print('100 + 200 =', add(100, 200))
    print('19 + 23 ...')
    try:
        add(19, 23)
    except ValueError as e:
        assert isinstance(e, SecretResultReached)
        print('Секретное число найдено')

    print()
    print('№5')
    print('screen size')
    screen = Screen(
        diagonal_inches=15.6,
        vertical_pixels=1920,
        horizontal_pixels=1080,
    )
    print('aspect ration(fractional):', screen.aspect_ratio)
    print('width:', screen.width)
    print('width (cm):',screen.width_cm)
    print('height:', screen.height)
    print('height (cm)', screen.height_cm)
    print('area:', screen.area)
    print('area (cm):', screen.area_cm)

    print()
    print('№6')
    print('valid parentheses:')
    valid_list = [
        '{}',
        "({})",
        '({[]})',
        '(()[])',
        '{()}[{}]',
        '{}()[]',
    ]
    invalid_list = [
        '{)',
        '(',
        ')',
        '({)}',
        '({[}])',
        '{()[}{}]',
        '{}(',
    ]
    for valid in valid_list:
        assert valid_parentheses(valid) is True
    for invalid in invalid_list:
        assert valid_parentheses(invalid) is False
    print('ok')