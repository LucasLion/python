from sys import argv

def building(string: str):
    upper_letters = 0
    lower_letters = 0
    punc_marks = 0
    spaces = 0
    digits = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            spaces += 1
        elif string[i].isalpha():
            if string[i].isupper():
                upper_letters += 1
            else:
                lower_letters += 1
        elif string[i].isdigit():
            digits += 1
        else:
            punc_marks += 1

    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punc_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    '''Checks all errors and exceptions'''
    try:
        assert len(argv) < 3, "more than one argument"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return

    string = ""
    if len(argv) < 2:
        string = input("What is the text to count?\n")
    else:
        string = argv[1]
    
    building(string)

if __name__ == "__main__":
    main();
