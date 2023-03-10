def pass_validator(password):

    pass_is_valid = True

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        pass_is_valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        pass_is_valid = False

    digit_counter = 0
    for character in password:
        if character.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        print("Password must have at least 2 digits")
        pass_is_valid = False

    return pass_is_valid

given_password = input()
password_is_valid = pass_validator(given_password)

if password_is_valid:
    print("Password is valid")