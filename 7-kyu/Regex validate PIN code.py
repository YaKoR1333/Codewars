def validate_pin(x):
    if (len(x) == 4 or len(x) == 6) and x.isdigit():
        return True
    else:
        return False
