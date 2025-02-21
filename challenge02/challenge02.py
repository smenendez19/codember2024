import os
import sys

logs_file = open(os.path.join(os.path.dirname(sys.argv[0]), "log.txt"), "r")

passwords_list = logs_file.read().split("\n")

sum_true = 0
sum_false = 0


def validate_password(password):
    char_appears = False
    last_number = None
    last_char = None
    for c in password:
        if str.isnumeric(c) and not char_appears:
            if not last_number:
                last_number = c
            else:
                if int(last_number) > int(c):
                    return False
                last_number = c
            continue
        elif str.isnumeric(c) and char_appears:
            return False
        elif not str.isnumeric(c):
            char_appears = True
            if not last_char:
                last_char = c
            else:
                if ord(last_char) > ord(c):
                    return False
                last_char = c
    return True


for password in passwords_list:
    validate = validate_password(password)
    if validate:
        sum_true += 1
    else:
        sum_false += 1

print(f"{sum_true}true{sum_false}false")
