import sys

def main():
    argc = len(sys.argv)
    assert argc <= 2, "more than one argument is provided"

    if argc == 1:
        print("What is the text to count?")
        try:
            input_str = sys.stdin.read()
        except EOFError:
            input_str = ""
    else:
        input_str = sys.argv[1]

    char_count = len(input_str)
    print(f"The text contains {char_count} characters:")

    upper_letters = 0
    lower_letters = 0
    punctuation_count = 0
    spaces_count = 0
    digits_count = 0

    for char in input_str:
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1
        elif char.isdigit():
            digits_count += 1
        elif char.isspace():
            spaces_count += 1
        else:
            punctuation_count += 1

    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{spaces_count} spaces")
    print(f"{digits_count} digits")

if __name__ == "__main__":
    main()