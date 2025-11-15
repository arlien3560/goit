from pathlib import Path

def total_salary(path) -> tuple[float, float]:
    salary_list = []

    try:
        file_path = Path(__file__).parent / path
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                salary = float(line.strip().split(',')[1])
                salary_list.append(salary)
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
    except PermissionError:
        print(f"Помилка: немає прав для читання файлу '{path}'")
    except Exception as e:
        print(f"Неочікувана помилка при читанні файлу: {e}")

    total_salary = sum(salary_list)
    average_salary = total_salary / len(salary_list) if salary_list else 0.0

    return total_salary, average_salary


def main(argv: list[str] | None = None) -> int:
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())