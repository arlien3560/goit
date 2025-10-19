from datetime import datetime, date

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    upcoming_birthdays = []

    for user in users:
        year, month, day = user['birthday'].split('.')
        day_for_birthday = date(int(year), int(month), int(day))

        now = datetime.now().date()
        next_birthday = date(now.year, day_for_birthday.month, day_for_birthday.day)

        difference = next_birthday - now

        if difference.days < 7:
            upcoming_birthdays.append(user)

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.10.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
