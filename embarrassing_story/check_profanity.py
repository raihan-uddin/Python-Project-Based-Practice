import urllib
from urllib import request
from urllib.parse import quote


def read_text():
    filepath = r"F:\PycharmProjects\UdacityPythonPractice\embarrassing_story\movie_quotes.txt";
    quotes = open(filepath, newline='', encoding='utf-8')
    contents_of_file = quotes.read()
    # print(contents_of_file)
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q=" + quote(text_to_check)
    with urllib.request.urlopen(url) as connection:
        output = connection.read().decode('utf-8')
        connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    connection.close()

# with urllib.request.urlopen('http://www.python.org/') as f:
#     print(f.read(900).decode('utf-8'))


read_text()