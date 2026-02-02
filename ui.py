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