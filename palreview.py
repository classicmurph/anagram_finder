import re
text = input("Give me a sentence: ")


def check_letters(text):
    new_text = text.lower()
    new_text = re.sub(r'[^A-Za-z]', "", new_text)
    while len(new_text) > 1:
        if new_text[0] == new_text[-1]:
            new_text = new_text[1:-1]
            return check_letters(new_text)
        else:
            return "{} is not a palindrome.".format(text)
    else:
        return "You've got a palindrome"

print(check_letters(text))
