import datetime
import os
from calendar import monthrange


def lookup_turns(year: int, month: int) -> list[tuple[str, str, bool]]:
    abs_turns = os.path.abspath("storage/turns.txt")
    abs_users = os.path.abspath("storage/users.txt")
    with open(abs_turns, "r") as f:
        turns = f.read().splitlines()
    with open(abs_users, "r") as f:
        users = f.read().splitlines()
    i = 0
    already_set = True
    full_next = "none"
    current_turn_user = "none"
    current_turn_initials = "none"
    next_turn_user = "none"
    next_turn_date = (1, 1, 1)
    _, num_days = monthrange(year, month)
    return_list = []
    for day in range(1, num_days + 1):
        current_date = (year, month, day)
        exact_match = False
        while after(current_date, next_turn_date) and i < len(turns):
            current_turn_user = next_turn_user
            next_turn_user, ny, nm, nd = turns[i].split()
            i += 1
            next_turn_date = (int(ny), int(nm), int(nd))
            already_set = False
        if after(current_date, next_turn_date):
            current_turn_user = next_turn_user
        if current_date == next_turn_date:
            exact_match = True
            current_turn_user = next_turn_user
        if not already_set:
            for j in range(len(users)):
                current_user, _, current_initials = users[j].split()
                if current_user == current_turn_user:
                    current_turn_initials = current_initials
                    full_next = turns[i-1] + "\n"
                    break
        return_list.append((current_turn_initials, full_next, exact_match))
    return return_list


def after(after: tuple[int, int, int], before: tuple[int, int, int]) -> bool:
    ayear, amonth, aday = after
    byear, bmonth, bday = before
    if ayear < byear:
        return False
    if ayear > byear:
        return True
    if amonth < bmonth:
        return False
    if amonth > bmonth:
        return True
    return aday > bday

def find_todays_phone():
    today = datetime.date.today()  # noqa: DTZ011
    abs_turns = os.path.abspath("storage/turns.txt")
    abs_users = os.path.abspath("storage/users.txt")
    with open(abs_turns, "r") as f:
        turns = f.read().splitlines()
    with open(abs_users, "r") as f:
        users = f.read().splitlines()

    last_turn_user = "none"
    for i in range(len(turns)):
        new_name, ny, nm, nd = turns[i].split()
        new_date = datetime.date(int(ny),int(nm),int(nd))
        if today >= new_date:
            last_turn_user = new_name
    for user in users:
        user_name, user_phone, _ = user.split()
        if user_name == last_turn_user:
            return user_phone
    return "not found"
