## Editorial
# Here the usage of ascii values is important
# While creating hash map/table substract 97 from the ascii value of the letter and add 1 to the index value which we get by substracting 97.


iter_value = "finding"
iter_obj = iter(iter_value)

H = [0 for _ in range(0,26)]

while True:
    try:
        item = next(iter_obj)
        ascii_value = ord(item) - 97
        H[ascii_value] = H[ascii_value] + 1

    except StopIteration:
        break

for index, value in enumerate(H):
    if value > 1:
        print (f"{chr(index+97)} is repeated {value} times")