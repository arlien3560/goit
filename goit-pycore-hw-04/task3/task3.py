import sys
from pathlib import Path
from colorama import Fore, Style, init

# Сумістність запуску на Windows
init(autoreset=True)


def visualize_directory_structure(directory_path: Path, prefix: str = "", is_last: bool = True):
    try:
        if not directory_path.exists():
            print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не існує")
            return
        
        if not directory_path.is_dir():
            print(f"{Fore.RED}Помилка: '{directory_path}' не є директорією")
            return
        
        try:
            items = sorted(directory_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        except PermissionError:
            print(f"{Fore.RED}Помилка: Немає прав доступу до '{directory_path}'")
            return
        
        for index, item in enumerate(items):
            is_last_item = (index == len(items) - 1)
            
            # Символи для гілок дерева
            if is_last_item:
                current_prefix = "┗ "
                next_prefix = "  "
            else:
                current_prefix = "┣ "
                next_prefix = "┃ "
            
            if item.is_dir():
                # Директорія - синій колір
                print(f"{prefix}{current_prefix}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                # Рекурсивно обробляємо піддиректорію
                visualize_directory_structure(item, prefix + next_prefix, is_last_item)
            else:
                # Файл - зелений колір
                print(f"{prefix}{current_prefix}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}Неочікувана помилка: {e}{Style.RESET_ALL}")


def main():
    """
    Головна функція скрипта.
    """
    # Перевіряємо аргументи командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python task3.py <шлях_до_директорії>{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Приклад: python task3.py /home/user/documents{Style.RESET_ALL}")
        return 1
    
    # Отримуємо шлях з аргументів
    directory_path = Path(sys.argv[1])
    
    # Виводимо назву кореневої директорії
    print(f"{Fore.CYAN}📦 {directory_path.name or directory_path}{Style.RESET_ALL}")
    
    # Візуалізуємо структуру
    visualize_directory_structure(directory_path)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())