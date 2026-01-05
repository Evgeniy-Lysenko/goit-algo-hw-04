# bot assistant

def parse_input(user_input): # parse the input
    cmd, *args = user_input.split() # split the input into command and arguments
    cmd = cmd.strip().lower() # remove leading and trailing whitespace and convert to lowercase
    return cmd, *args

def add_contact(args, contacts): # add contact
    name, phone = args # get name and phone
    contacts[name] = phone # add to contacts dictionary
    return "Contact added."

def change_contact(args, contacts): # change contact
    name, phone = args # get name and phone
    if name in contacts: # check if contact exists
        contacts[name] = phone # update contact
        return "Contact updated."
    else:
        return "Contact not found."
    
def contact_phone(args, contacts): # get contact phone
    name = args[0] # get name
    return contacts.get(name, "Contact not found.") # return phone or "Contact not found."

def all_contacts(contacts): # get all contacts
    if not contacts: # check if contacts dictionary is empty
       return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in sorted(contacts.items())) # return all sorted contacts
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ") # get user input
        command, *args = parse_input(user_input) # parse the input

        if command in ["close", "exit"]: # exit commands
            print("Good bye!")
            break
        elif command == "hello": # hello command
            print("How can I help you?")
        elif command == "add": # add command
            print(add_contact(args, contacts))
        elif command == "change": # change command
            print(change_contact(args, contacts))
        elif command == "phone": # phone command
            print(contact_phone(args, contacts))
        elif command == "all": # all command
            print(all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

