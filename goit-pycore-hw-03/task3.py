import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонні номери до стандартного формату.
    
    Args:
        phone_number (str): Рядок з телефонним номером у будь-якому форматі
    
    Returns:
        str: Нормалізований телефонний номер у форматі '+380XXXXXXXXX'
    
    Examples:
        >>> normalize_phone("067\\t123 4567")
        '+380671234567'
        >>> normalize_phone("+380 44 123 4567")
        '+380441234567'
        >>> normalize_phone("0503451234")
        '+380503451234'
    """
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    if cleaned_number.startswith('+'):
        return cleaned_number
    elif cleaned_number.startswith('380'):
        return '+' + cleaned_number
    else:
        return '+38' + cleaned_number


# Тестування
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Додаткові тести для перевірки
print("\n--- Додаткові тести ---")
test_cases = [
    ("050 123 45 67", "+380501234567"),
    ("+38 050 123 45 67", "+380501234567"),
    ("380501234567", "+380501234567"),
    ("  +380 (50) 123-45-67  ", "+380501234567"),
]

for test_input, expected in test_cases:
    result = normalize_phone(test_input)
    status = "✓" if result == expected else "✗"
    print(f"{status} {test_input:30} -> {result:20} (очікується: {expected})")