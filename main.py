from ui import *
from funcs import *




if __name__ == "__main__":
    while True:
        display_menu()
        choice = user_choice()
        if choice == "6":
            exit()
            break

        jf_content = read_json_file("contact_book.json")

        if choice == "1":
            name, phone_number = user_add_contact()
            if add_contact(name, phone_number, "contact_book.json", jf_content):
                print("Operation succeeded!")
            else:
                print("Oops, something went wrong!")

        elif choice == "2":
            display_all_contacts(jf_content)
