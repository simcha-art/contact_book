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





def add_contact(name: str, phone_number: str, json_file_name: str, json_file_content: dict|list):
    try:
        new_contact = {"name": name, "phone_number": phone_number}
        json_file_content.append(new_contact)
        with open(json_file_name, "w") as jf:
            json.dump(json_file_content, jf, indent=4)
        return True
    except:
        return False


def find_contact(name: str, json_file_content: dict|list):
    for contact in json_file_content:
        if contact["name"] == name:
            return contact
    return False

def delete_contact(name: str, jf_content: list[dict], json_file_name):
    try:
        for contant in jf_content:
            if contant["name"] == name:
                jf_content.remove(contant)
                with open(json_file_name, "w") as jfile:
                    json.dump(jf_content, jfile)
                    return True
        return False
    except Exception as e:
        print(f"Error: {e}")


