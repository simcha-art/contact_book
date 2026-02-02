from ui import *
from funcs import *




if __name__ == "__main__":
    while True:
        display_menu()
        choice = user_choice()
        if choice == "6":
            exit()
            break

        jf_name = "contact_book.json"
        jf_content = read_json_file(jf_name)

        if choice == "1":
            name, phone_number = user_add_contact()
            status = add_contact(name, phone_number, jf_name, jf_content)
            display_operation_status(status)

        elif choice == "2":
            display_all_contacts(jf_content)

        elif choice == "3":
            name = receive_contact_name()
            contact = find_contact(name, jf_content)
            display_contact(contact)

        elif choice == "4":
            name = receive_contact_name()
            status = delete_contact(name, jf_content, jf_name)
            display_operation_status(status)

        elif choice == "5":
            name = receive_contact_name()
            contact = find_contact(name, jf_content)
            if not contact:
                display_contact(contact)
                continue
            edit_choice = edit_options()
            if edit_choice == "1":
                phone_number = receive_contact_number()
                status = edit_contact(contact, phone_number, jf_content, jf_name)
                display_operation_status(status)
            elif edit_choice == "2":
                email_address = receive_contact_email()
                status = add_email(contact, email_address, jf_content, jf_name)
                display_operation_status(status)
            display_contact(contact)

