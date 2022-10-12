import regex


def is_valid_email_1(email):
    """
    This version tests that the email starts with a letter, contains an "@", and ends with ".edu" or ".ac".
    It doesn't have any false negatives, but it does suffer from false positives.
    """

    return (
        email[0].isalpha()
        and "@" in email
        and email.endswith(".edu")
        or email.endswith(".ac")
    )


def is_valid_email_2(email):
    """
    This version refactors the code to use regex, which is more robus, but doesn't handle the TypeError.
    """

    return regex.compile(r"^[a-z][a-z\d_]+@[a-z]+\.((edu)|(ac))$").match(email)


def is_valid_email_3(email):
    """
    This is the final version, which handles the TypeError and uses regex.
    """

    if type(email) != str:
        raise TypeError("email must be a string")

    return regex.compile(r"^[a-z][a-z\d_]+@[a-z]+\.((edu)|(ac))$").match(email)
