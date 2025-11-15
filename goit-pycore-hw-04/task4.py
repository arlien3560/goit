def parse_input(user_input):
    """Парсить введений користувачем рядок на команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """Додає новий контакт до словника."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту."""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} not found."


def show_phone(args, contacts):
    """Показує номер телефону для зазначеного контакту."""
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} not found."


def show_all(contacts):
    """Виводить всі збережені контакти."""
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    # Словник команд та відповідних функцій
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all
    }
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command in commands:
            # Викликаємо функцію зі словника
            if command == "all":
                print(commands[command](contacts))
            else:
                print(commands[command](args, contacts))
        
        else:
            print("Invalid command.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())