from pathlib import Path

def get_cats_info(path) -> list[dict[str, str]]:
    cats = []

    try:
        file_path = Path(__file__).parent / path
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cats.append({'id': id, 'name': name, 'age': int(age)})
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
    except PermissionError:
        print(f"Помилка: немає прав для читання файлу '{path}'")
    except Exception as e:
        print(f"Неочікувана помилка при читанні файлу: {e}")

    return cats

def main(argv: list[str] | None = None) -> int:
    cats_info = get_cats_info("cats.txt")
    print(cats_info)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())