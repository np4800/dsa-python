## Description: Check if the given string is valid or not
# Editorial:
    ## while traversing the character in a given string if the letter does NOT fall in the ascii range
    ## of character then it is called the invalid string
from typing import Iterable

def isValid(name):
    iterable_value= name
    iterable_obj = iter(iterable_value)

    while True:
        try:
            item = next(iterable_obj)
            if ord(item) >= 65 and ord(item) <= 90:
                pass
            elif ord(item) >= 97 and ord(item) <= 122:
                pass
            else:
                print(ord(item))
                return False
        except StopIteration:
            return True


print(isValid('Anil'))