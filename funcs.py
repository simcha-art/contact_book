import json

def read_json_file(json_file):
    try:
        with open(json_file) as jf:
            content = json.load(jf)
    except FileNotFoundError:
        with open(json_file, "w") as jf:
            json.dump([], jf)
        with open(json_file) as jf:
            content = json.load(jf)
    return content

jf_content = read_json_file("contact_book.json")




def add_contact(name: str, phone_number: str, json_file_name: str, json_file_content: dict|list):
    new_contact = {"name": name, "phone_number": phone_number}
    json_file_content.append(new_contact)
    with open(json_file_name, "w") as jf:
        json.dump(json_file_content, jf, indent=4)

add_contact("simcha copperman", "0548473666", "contact_book.json", jf_content)