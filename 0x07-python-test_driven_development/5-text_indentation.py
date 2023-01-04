#!/usr/bin/python3
def text_indentation(text):
    """
    function that prints a text with 2 new lines
        after each of these characters: ., ? and :

    There should be no space at the beginning or
        at the end of each printed line
    """
    new_text = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    for item in text:
        if item in ".:?":
            if text[i + 1] == " ":
                text = text[:i + 1] + text[i + 2:]
        else:
            i += 1
    for j in text:
        print(j, end="")
        if j in ('.', '?', ':'):
            print("\n")
