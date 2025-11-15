from datetime import datetime, date

def get_days_from_today(end_date_string: str) -> int:
    """
    Розраховує кількість днів між заданою датою і поточною датою.
    
    Args:
        date (str): Рядок дати у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09')
    
    Returns:
        int: Кількість днів від заданої дати до поточної дати.
             Позитивне число - якщо задана дата в минулому.
             Від'ємне число - якщо задана дата в майбутньому.
             
    Raises:
        ValueError: Якщо формат дати неправильний
    """

    today = date.today()
    try:
        end_date = datetime.strptime(end_date_string, '%Y-%m-%d').date()
        difference = today - end_date
        
        return difference.days        
    except ValueError as error:
        raise ValueError(f"Неправильний формат дати. Очікується 'РРРР-ММ-ДД', отримано: '{end_date_string}'") from error


if __name__ == '__main__':
    print(get_days_from_today('2026-01-23'))
    print(get_days_from_today('2025-11-30'))
    print(get_days_from_today('2025-09-23'))