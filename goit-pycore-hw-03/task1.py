from datetime import date, timedelta

def get_days_from_today(start_date: date, end_date: date) -> int:
    difference = (end_date - start_date).days + 1
    weeks = difference // 7
    days_left = difference % 7

    weeks_result = weeks * 2

    current_date = start_date + timedelta(days=weeks * 7)

    for i in range(days_left):
        if current_date.weekday() in [5, 6]:
            weeks_result += 1
        current_date += timedelta(days=1)
    
    return weeks_result


if __name__ == '__main__':
    assert get_days_from_today(date(2013, 9, 18), date(2013, 9, 23)) == 2 #"1st example"
    assert get_days_from_today(date(2013, 1, 1), date(2013, 2, 1)) == 8 #"2nd example"
    assert get_days_from_today(date(2013, 2, 2), date(2013, 2, 3)) == 2 #"3rd example"