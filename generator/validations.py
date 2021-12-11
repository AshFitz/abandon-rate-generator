def validate_text(input_value):
    if not input_value:
        return False
    elif all(x.isalpha() or x.isspace() for x in input_value):
        return True
    else:
        return False


def validate_numbers(input_value):
    return False