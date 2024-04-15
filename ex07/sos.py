import sys

NESTED_MORSE = {
  " ": "/ ",
  "A": ".- ", "B": "-...",
  "C": "-.-.", "D": "-..", "E": ".",
  "F": "..-.", "G": "--.", "H": "....",
  "I": "..", "J": ".---", "K": "-.-",
  "L": ".-..", "M": "--", "N": "-.",
  "O": "---", "P": ".--.", "Q": "--.-",
  "R": ".-.", "S": "...", "T": "-",
  "U": "..-", "V": "...-", "W": ".--",
  "X": "-..-", "Y": "-.--", "Z": "--..",
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
  "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "....-"
}

def text_to_morse(text):

    morse = ""
    for char in text:
        morse += NESTED_MORSE[char.upper()]
    print(morse)

def main():
    """
    Accepts only 1 argument:
    1. string

    prints the morse code of the string.
    """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        for char in sys.argv[1]:
            assert char.isalnum() or char.isspace(), "the arguments are bad"
    except AssertionError as e:
        print(e)
        sys.exit(1)

    text_to_morse(sys.argv[1])

if __name__ == "__main__":
    main()
