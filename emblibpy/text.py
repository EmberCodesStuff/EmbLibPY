from random import randint

def weirdCase(text: str):
    """Randomly changes each character to uppercase or lowercase."""
    result = ""
    for char in text:
        if randint(0, 1) == 0: result += char.lower()
        else: result += char.upper()
    return result

def scramble(text: str):
    """Randomly rearranges the characters in the given text."""
    result = ""
    for char in text:
        if randint(0, 1) == 0: result += char
        else: result = char + result 
    return result

def skillIssue():
    """'Skill issue'."""
    print("Skill issue")
    return "Skill issue"
    