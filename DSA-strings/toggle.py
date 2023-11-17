## Here the ascii value of the letter can be found using the python inbuilt functions like chr() and ord()


from typing import Iterable


iterable_value = "GeeKs"
iterable_obj = iter(iterable_value)
toggle_string=""
while True:
    try:
        item = next(iterable_obj)
        if ord(item) >= 65 and ord(item) <=97:
            print(chr(ord(item)+32))
            toggle_string = toggle_string + chr(ord(item)+32)
        else:
            print(chr(ord(item)-32))
            toggle_string = toggle_string + chr(ord(item)-32)
    except StopIteration:
        break

print(toggle_string)