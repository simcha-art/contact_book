def display_menu():
    print("=== Contact Book ===")
    print("1. Add contact\n"
          "2. Show all contacts\n"
          "3. Search contact\n"
          "4. Delete contact\n"
          "5. Edit contact\n"
          "6. Exit")

def display_message(message):
    print()
    print("=" * len(message) if len(message) < 40 else "=" * 40)
    print(message)
    print("=" * len(message) if len(message) < 40 else "=" * 40)
    print()


def user_choice():
    choose = input("choose option: ")
    return choose

def user_add_contact():
    name = input("please enter contact's name: ")
    phone_number = input("please enter contact's phone_number: ")
    return name, phone_number

def receive_contact_number():
    phone_number = input("please enter contact's phone number: ")
    return phone_number

def receive_contact_name():
    name = input("please enter contact's name: ")
    return name

def exit():
    message = "See yot next time :)"
    display_message(message)

def display_all_contacts(json_file_content):
    message = ""
    for contact in json_file_content:
        message += f"{contact["name"]}: {contact["phone_number"]} {("("+ contact["Email_address"] +") ") if contact["Email_address"] else ""}\n"
    message = message[:-1]
    display_message(message)

def display_contact(contact: dict):
    if contact:
        message = f"{contact["name"]}: {contact["phone_number"]} {("("+ contact["Email_address"] +")") if contact["Email_address"] else ""}"
    else:
        message = "Contact didn't found"
    display_message(message)

def display_operation_status(status: bool):
    message = "operation succeeded!" if status else "oops, something went rong"
    display_message(message)

def edit_options():
    message = ("1. changing number\n"
               "2. adding/changing email address")
    display_message(message)
    choice = input("enter your choice: ")
    return choice

def receive_contact_email():
    email = input("enter email address: ")
    return email