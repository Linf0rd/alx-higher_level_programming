#!/usr/bin/python3
"""
A text indentation function.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char
        if char in ['.', '?', ':']:
            new_text += "\n\n"

    print("\n".join(line.strip() for line in new_text.split("\n")))
