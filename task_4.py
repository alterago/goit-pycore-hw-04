"""Task 4: a console assistant bot that keeps a phone book.

Commands (case-insensitive): hello, add <name> <phone>, change <name> <phone>,
phone <name>, all, close / exit. Ctrl+C or Ctrl+D also exits.
"""

Contacts = dict[str, str]


def parse_input(user_input: str) -> tuple[str, ...]:
    """Split the input into a lower-case command and its arguments."""
    parts = user_input.split()
    if not parts:
        return ("",)
    cmd, *args = parts
    return cmd.strip().lower(), *args


def find_name(contacts: Contacts, name: str) -> str | None:
    """Return the stored name that matches ``name`` regardless of case."""
    return next((stored for stored in contacts if stored.lower() == name.lower()), None)


def add_contact(args: list[str], contacts: Contacts) -> str:
    """Add a contact; an existing name (in any case) gets the new phone."""
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    stored_name = find_name(contacts, name) or name
    contacts[stored_name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: Contacts) -> str:
    """Change the phone of an existing contact."""
    if len(args) != 2:
        return "Usage: change <name> <phone>"
    name, phone = args
    stored_name = find_name(contacts, name)
    if stored_name is None:
        return f"Contact '{name}' not found."
    contacts[stored_name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: Contacts) -> str:
    """Return the phone of the contact."""
    if len(args) != 1:
        return "Usage: phone <name>"
    stored_name = find_name(contacts, args[0])
    if stored_name is None:
        return f"Contact '{args[0]}' not found."
    return contacts[stored_name]


def show_all(contacts: Contacts) -> str:
    """Return all contacts, one per line."""
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: Contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C or Ctrl+D ends the bot the same way as "exit".
            print("\nGood bye!")
            break
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
