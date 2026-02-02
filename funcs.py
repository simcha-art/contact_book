import json

def read_json_file(json_file):
    try:
        with open(json_file) as jf:
            content = json.load(jf)
    except FileNotFoundError:
        with open(json_file, "w") as jf:
            json.dump(None, jf)
        with open(json_file) as jf:
            content = json.load(jf)
    return content

read_json_file("contact_book.json")



# def add_contact(name: str, phone_number: str, json_script: str):
