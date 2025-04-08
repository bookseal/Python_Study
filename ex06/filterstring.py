import sys
from ft_filter import ft_filter 

def main(argc, argv):
    '''
    This program filters a string based on the length of its words.
    It takes two arguments:
    1. A string containing words separated by spaces.
    2. An integer representing the minimum length of words to keep.
    The program will print a list of words that are longer than the specified length.
    '''
    # Assert that the number of arguments is correct
    assert argc == 3, "AssertionError: The program requires exactly 2 arguments.\nUsage: python filterstring.py '<string>' <number>'"

    try:
        # Extract the arguments
        input_string = argv[1]
        input_number = int(argv[2])  # This will raise a ValueError if not an integer

        # Assert the types of the arguments
        assert isinstance(input_string, str), "AssertionError: The first argument must be a string."
        assert isinstance(input_number, int), "AssertionError: The second argument must be an integer."

        # Split input_string into a list of words
        words = input_string.split(' ')
        # Filter the words based on their length
        filtered_words = ft_filter(lambda x: len(x) > input_number, words)
        # Display the list of filtered words
        print(list(filtered_words))  # Convert the filter object to a list for display
    except ValueError:
        raise AssertionError("AssertionError: The second argument must be an integer.")

if __name__ == "__main__":
    # print(filter.__doc__)
    # print(ft_filter.__doc__)
    main(len(sys.argv), sys.argv)

