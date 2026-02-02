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
    print("=" * len(message) if len(message) < 30 else "=" * 30)
    print(message)
    print("=" * len(message) if len(message) < 30 else "=" * 30)
    print()


def user_choice():
    choose = input("choose option: ")
    return choose

def user_add_contact():
    name = input("please enter contact's name: ")
    phone_number = input("please enter contact's phone_number: ")
    return name, phone_number

def receive_contant_number():
    phone_number = input("please enter contant's phone number: ")
    return phone_number

def receive_contact_name():
    name = input("please enter contact's name: ")
    return name

def exit():
    message = "See yot next time :)"
    display_message(message)

def display_all_contacts(json_file_content):
    message = ""
    for contant in json_file_content:
        message += f"{contant["name"]}: {contant["phone_number"]} {(" ," + contant["Email_address"]) if contant["Email_address"] else ""}\n"
    message = message[:-2]
    display_message(message)

def display_contact(contact: dict):
    if contact:
        message = f"{contact["name"]}: {contact["phone_number"]}"
    else:
        message = "Contact didn't found"
    display_message(message)

def display_operation_status(status: bool):
    message = "operation succeeded!" if status else "oops, something went rong"
    display_message(message)


