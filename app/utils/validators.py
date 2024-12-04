import re
# these validators not for all data
# i'm just checkin if it workin wit this
def validate_full_name(full_name):
    """Проверяет, что ФИО состоит из трёх слов."""
    if len(full_name.split()) != 3:
        return False, "Full Name must include exactly three words (e.g., Firstname Middlename Lastname)."
    return True, ""

def validate_email(email):
    """Проверяет, что email имеет правильный формат."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        return False, "Invalid email format."
    return True, ""

def validate_nickname(nickname):
    """Проверяет, что никнейм состоит из менее чем 50 символов."""
    if len(nickname) > 50:
        return False, "Nickname must be less than 50 characters."
    return True, ""

def validate_passwords(password, confirm_password):
    """Проверяет совпадение пароля и длину."""
    if password != confirm_password:
        return False, "Passwords do not match."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, ""

def validate_phone_number(phone_number):
    """Проверяет формат телефона (опционально)."""
    if phone_number and not re.match(r"^\+?\d{10,15}$", phone_number):
        return False, "Phone number must be valid (e.g., +1234567890)."
    return True, ""

def validate_date_of_birth(date_of_birth):
    """Проверяет, что дата рождения введена."""
    if not date_of_birth:
        return False, "Date of birth is required."
    return True, ""

def validate_accept_policy(accept_policy):
    """Проверяет, что политика сайта принята."""
    if not accept_policy:
        return False, "You must accept the site policy."
    return True, ""
