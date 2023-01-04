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
    for i in text:
        new_text = 
        if i in ('.', '?', ':'):
            print("\n")
            lstrip()
