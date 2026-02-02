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
            status = add_contact(name, phone_number, "contact_book.json", jf_content)
            display_operation_status(status)

        elif choice == "2":
            display_all_contacts(jf_content)

        elif choice == "3":
            name = receive_contact_name()
            contact = find_contact(name, jf_content)
            display_contact(contact)

        elif choice == "4":
            name = receive_contact_name()
            status = delete_contact(name, jf_content, "contact_book.json")
            display_operation_status(status)

        elif choice == "5":
            name = receive_contact_name()
            contact = find_contact(name, jf_content)
            if not contact:
                display_contact(contact)
                continue
            phone_number = receive_contant_number()
            status = edit_contact(contact, phone_number, jf_content, "contact_book.json")
            display_operation_status(status)
            display_contact(contact)

