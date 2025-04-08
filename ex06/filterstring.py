import sys
from ft_filter import ft_filter


def main(argc, argv):
    '''
    This program filters a string based on the length of its words.
    It takes two arguments:
    1. A string containing words separated by spaces.
    2. An integer representing the minimum length of words to keep.
    '''
    # Assert that the number of arguments is correct
    assert argc == 3, "The program requires 2 arguments."

    try:
        # Extract the arguments
        input_str = argv[1]
        input_num = int(argv[2])

        # Assert the types of the arguments
        assert isinstance(input_str, str), "The first argument must be a str."
        assert isinstance(input_num, int), "The second argument must be an int"

        # Split input_string into a list of words
        words = input_str.split(' ')
        # Filter the words based on their length
        filtered_words = ft_filter(lambda x: len(x) > input_num, words)
        # Display the list of filtered words
        print(list(filtered_words))
    except ValueError:
        raise AssertionError("The second argument must be an integer.")


if __name__ == "__main__":
    # print(filter.__doc__)
    # print(ft_filter.__doc__)

    main(len(sys.argv), sys.argv)
