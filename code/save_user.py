import os


def save_user(name_string, phone_string, initials_string):
    name = name_string.get()
    initials = initials_string.get()
    phone = phone_string.get()
    print(f"name: {name} phone: {phone} initials: {initials}")
