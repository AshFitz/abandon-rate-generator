"""
Function to takes one parameter when being called,
ensures the user input is not empty, has only
alphabetical strings and allow spaces.
"""


def validate_text(input_value):
    if not input_value:
        return False
    elif all(x.isalpha() or x.isspace() for x in input_value):
        return True
    else:
        return False


"""
Function to takes one parameter when being called,
ensures the user input is not empty, uses the
isdigit method to check the input only consists of
numbers.
"""


def validate_numbers(input_value):
    if not input_value:
        return False
    elif all(z.isdigit() for z in input_value):
        return True
    else:
        return False
