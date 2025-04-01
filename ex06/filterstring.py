import sys
from ft_filter import ft_filter 

def main(argc, argv):
    # Assert when argv is not 3
    assert argc == 3, "the arguments are bad"
    
    try:
        # Extract the string and the number from the arguments
        input_string = argv[1]
        input_number = int(argv[2])

        # split input_string into a list of words
        words = input_string.split(' ')
        # Filter the words based on the length
        filtered_words = ft_filter(lambda x: len(x) > input_number, words)
        # Display the list of filtered words
        print(filtered_words)
    except ValueError:
        print("Error: Please provide a valid string and an integer.")

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)

