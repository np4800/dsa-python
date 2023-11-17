iter_value = "How are you?"
iter_obj = iter(iter_value)
word = 0
while True:
    try:
        item = next(iter_obj) 
        if item == " ":  ## Edge Case: if the there are more than 1 white space then you have to check if the previous character was a white space or not. Here it will be and condition
            word = word + 1
    except StopIteration:
        break

print(f"No. of word in a sentence are: {word+1}")

## Count the number of vowels?
# Editorial
    ## you can use the simple if else statement like if current letter is in (a,e,i,o,u)
    ## you can use the range of the Ascii values of the letter to check if the letter is consonent or not


