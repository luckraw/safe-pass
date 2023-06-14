import secrets
import string


def generate_password(length, min_special_chars=1, min_numbers=1, min_uppercase_letters=1, excluded_chars=''):
    special_chars = string.punctuation.translate(str.maketrans('', '', excluded_chars))
    numbers = string.digits.translate(str.maketrans('', '', excluded_chars))
    uppercase_letters = string.ascii_uppercase.translate(str.maketrans('', '', excluded_chars))

    password = ''
    while True:
        password = ''.join(
            secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        if (
                sum(char in special_chars for char in password) >= min_special_chars and
                sum(char in numbers for char in password) >= min_numbers and
                sum(char in uppercase_letters for char in password) >= min_uppercase_letters and
                password.translate(str.maketrans('', '', excluded_chars)) == password
        ):
            break

    return password


def contains_special_char(password):
    special_chars = string.punctuation
    for char in password:
        if char in special_chars:
            return True
    return False


def contains_number(password):
    numbers = string.digits
    for char in password:
        if char in numbers:
            return True
    return False


def contains_uppercase_letter(password):
    uppercase_letters = string.ascii_uppercase
    for char in password:
        if char in uppercase_letters:
            return True
    return False


def validate_password(password):
    min_length = 8
    min_special_chars = 1
    min_numbers = 1
    min_uppercase_letters = 1

    if len(password) < min_length:
        return False

    if (
            not contains_special_char(password) or
            not contains_number(password) or
            not contains_uppercase_letter(password)
    ):
        return False

    return True


def main():
    length = int(input("Enter the desired password length: "))
    min_special_chars = int(input("Enter the minimum number of special characters in the password: "))
    min_numbers = int(input("Enter the minimum number of numbers in the password: "))
    min_uppercase_letters = int(input("Enter the minimum number of uppercase letters in the password: "))
    excluded_chars = input("Enter the characters to be excluded from the password (optional): ")

    password = generate_password(length, min_special_chars, min_numbers, min_uppercase_letters, excluded_chars)

    print("Generated password:", password)

    if validate_password(password):
        print("Valid password!")
    else:
        print("Invalid password!")


if __name__ == '__main__':
    main()
