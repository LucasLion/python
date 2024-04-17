from sys import argv


def whatis():
    if int(argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():

    if len(argv) == 1:
        return
    try:
        assert len(argv) <= 2, "more than one argument is provided"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return
    try:
        assert argv[1].lstrip("-").isdigit(), "argument is not an integer"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return
    whatis()


if __name__ == "__main__":
    main()
