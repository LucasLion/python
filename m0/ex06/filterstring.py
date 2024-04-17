import sys
from ft_filter import ft_filter


def filterstring(string, number):
    # split string by spaces
    string = string.split()
    # lamba function for a string length to be lower than the number
    print(list(ft_filter(lambda x: len(x) > int(number), string)))


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer

    Returns a list of words that are longer than the integer.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        n = int(sys.argv[2])
        if not isinstance(sys.argv[1], str) or not isinstance(n, int):
            raise AssertionError("the arguments are bad")

        filterstring(sys.argv[1], sys.argv[2])

    except ValueError as msg:
        print(f"ValueError: {msg}")
        return
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return


if __name__ == '__main__':
    main()
