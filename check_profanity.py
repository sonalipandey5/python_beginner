import urllib
def read_text():
    quotes = open("C:\Users\Dell\Desktop\movie_quotes.txt")
    content=quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_speech):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_speech)
    output=connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("This document has no error!")
    else:
        print("could not scan the document properly")

read_text()


