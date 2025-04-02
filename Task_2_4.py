def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) !=2:
        return "Invalid input"

    name, phone = args
    if name not in contacts:
        return f"Contact with me {name} not found"

    contacts[name] = phone
    return f"Contact {name} updated"

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid input"
    
    name = args[0]
    if name not in contacts:
        return f"Contact with me {name}  not found"
    
    return f"{name}: {contacts[name]}"

def show_all(contacts):
    """Показ всіх контактів із номерами телефонів."""
    if not contacts:
        return "No contacts available."
    
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "change":  
            print(change_contact(args, contacts))
        elif command == "phone":  
            print(show_phone(args, contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":  
            print(show_all(contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
