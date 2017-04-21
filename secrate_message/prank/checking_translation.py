#!/usr/bin/python3
import os

'''
intab  = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example ... wow!!"
print(str.translate(trantab))

file_name = "012sfdsfdds.jpg"
text = file_name.translate(str.maketrans('','','0123456789'))
print(text)
'''

# file not exist
'''
folder_path = r"F:\PycharmProjects\UdacityPythonPractice\secrate_message\prank\prank"
# this file is not exist
file_name = "ath1ens.jpg"
# Error throw : FileNotFoundError: [WinError 2] The system cannot find the file specified: 'ath1ens.jpg' -> 'athens.jpg'
os.chdir(folder_path)
try:
    os.rename(file_name, file_name.translate(str.maketrans('', '', '0123456789')))
except IOError:
    print("Error: can\'t find file for exception handeling")
'''



# Duplicate File
folder_path = r"F:\PycharmProjects\UdacityPythonPractice\secrate_message\prank\prank"
file_name = "ath1ens.jpg"
# Error throw : FileNotFoundError: [WinError 2] The system cannot find the file specified: 'ath1ens.jpg' -> 'chicago.jpg'
os.chdir(folder_path)
try:
    os.rename(file_name, "chicago.jpg")
except IOError:
    print("Error: there is a file with same name")
