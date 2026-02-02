def display_menu():
    print("=== Contact Book ===")
    print("1. Add contact\n"
          "2. Show all contacts\n"
          "3. Search contact\n"
          "4. Delete contact\n"
          "5. Edit contact\n"
          "6. Exit")


def user_choice():
    choose = input("choose option: ")
    return choose

def user_add_contact():
    name = input("please enter contact's name: ")
    phone_number = input("please enter contact's phone_number: ")
    return name, phone_number

def exit():
    print("See yot next time :)")

def display_all_contacts(json_file_content):
    print()
    print("==========================")
    for contant in json_file_content:
        print(f"{contant["name"]}: {contant["phone_number"]}")
    print("==========================")
    print()
