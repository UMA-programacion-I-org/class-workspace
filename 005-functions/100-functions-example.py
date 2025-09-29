def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return not is_even(number)


def mean(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers) if numbers else 0
