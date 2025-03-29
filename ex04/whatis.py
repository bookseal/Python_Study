import sys


def main():
    argc = len(sys.argv)

    argv = sys.argv
    assert argc <= 2, "more than one argument is provided"
    assert argv[1].isdigit() or (argv[1][0] in '+-' and argv[1][1:].isdigit()), "argument is not an integer"

    if argc == 1:
        return
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()