import os


def save_user(name_string, phone_string, initials_string, output_string, users):
    name = name_string.get()
    name = name.replace(" ", "_")
    initials = initials_string.get()
    phone = phone_string.get()
    abs_users = os.path.abspath("storage/users.txt")
    with open(abs_users, "r") as f:
        content = f.read()
    if check_for_duplicates(name):
        output_string.set("error: new user name cannot be the same as existing user")
        return
    if phone == "":
        output_string.set("error: phone number must be set")
        return
    if initials == "":
        output_string.set("error: initials must be set")
        return
    if not phone.isdigit():
        output_string.set("error: phone number must contain only numbers")
        return
    if name == "":
        output_string.set("error: name must be set")
        return

    content = content + f"{name} {phone} {initials}\n"
    with open(abs_users, "w") as f:
        f.write(content)
    users.generate()
    output_string.set("user saved")

def check_for_duplicates(new_name:str)->bool:
    abs_users = os.path.abspath("storage/users.txt")
    with open(abs_users, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for line in lines:
        name, _, _ = line.split()
        if name == new_name:
            return True
    return False
