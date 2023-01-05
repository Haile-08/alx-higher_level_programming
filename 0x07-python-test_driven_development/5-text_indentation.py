#!/usr/bin/python3

def text_indentation(text):
    """text indentaion
    Args:
        text: input text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
