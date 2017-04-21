#!/usr/bin/python3
import string

intab  = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example ... wow!!"
print(str.translate(trantab))

file_name = "012sfdsfdds.jpg"
text = file_name.translate(str.maketrans('','','0123456789'))
print(text)
