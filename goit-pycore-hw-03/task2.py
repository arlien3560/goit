import random

def get_numbers_ticket(min: int, max: int, quantity: int) ->list[int]:
    """
    Генерує набір унікальних випадкових чисел для лотереї.
    
    Args:
        min (int): Мінімальне можливе число у наборі (не менше 1)
        max (int): Максимальне можливе число у наборі (не більше 1000)
        quantity (int): Кількість чисел, які потрібно вибрати
    
    Returns:
        list: Відсортований список унікальних випадкових чисел.
              Повертає пустий список, якщо параметри некоректні.
    
    Examples:
        >>> numbers = get_numbers_ticket(1, 49, 6)
        >>> len(numbers)
        6
        >>> all(1 <= num <= 49 for num in numbers)
        True
    """
    # Перевірка коректності вхідних параметрів
    if min < 1:
        return []
    
    if max > 1000:
        return []
    
    if min >= max:
        return []
    
    if quantity < 1:
        return []
    
    # Перевірка, чи можливо вибрати задану кількість унікальних чисел
    if quantity > (max - min + 1):
        return []

    mix_range = range(min, max + 1)
    numbers = random.sample(mix_range, quantity)
    numbers.sort()
    
    return numbers

test_cases = [(1, 49, 6), (10, 4, 5), (10, 14, 6), (-10, 10, 5), (1000, 1200, 3)]

for min, max, quantity in test_cases:
    lottery_numbers = get_numbers_ticket(min, max, quantity)
    print("Ваші лотерейні числа:", lottery_numbers)

