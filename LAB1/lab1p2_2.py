# Uses the extended slice syntax from https://stackoverflow.com/questions/931092/reverse-a-string-in-python

file = open("in.txt", "r")

raw_text = file.read()

result = "No"

# Alphanumeric char checking based on code here: https://www.w3schools.com/python/ref_string_isalnum.asp

def alnum_filter(text):
    filtered_text = ""

    for char in text:
        if (char.isalnum()):
            filtered_text = filtered_text + char

    return filtered_text

filtered_text = alnum_filter(raw_text)

text_len = len(filtered_text)

if (text_len % 2 == 0):
    first_half = filtered_text[:text_len/2]
    sec_half = filtered_text[text_len/2:]

    sec_half_rev = sec_half[::-1]

    if (first_half == sec_half_rev):
        result = "Yes"



print(result)
