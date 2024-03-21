

from sys import argv

def isEvenOrOdd():

    assert len(argv) == 2, "argument is not an integer"
    assert argv[1].isdigit(), "more than one argument is provided"

    if int(argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.");

isEvenOrOdd();
