import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--.."
}

def morse_code(message):
    """
    Convert a message to Morse code.
    """
    morse_code_message = ""
    for char in message.upper():
        print(f"char: {char}")
        if char not in NESTED_MORSE:
            raise AssertionError("Invalid character in message")

        if char in NESTED_MORSE:
            morse_code_message += NESTED_MORSE[char] + " "
        else:
            morse_code_message += char
    return morse_code_message.strip()

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    assert argc == 2, "Usage: python sos.py <message>"

    message = argv[1]
    
    morse_code_message = morse_code(message)
    print(f"{morse_code_message}")