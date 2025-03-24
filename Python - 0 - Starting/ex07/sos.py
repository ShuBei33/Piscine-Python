import sys


NESTED_MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....', 'I': '..',  'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',   'N': '-.',  'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',  'S': '...', 'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..',  
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def main():
    """
    Catch errors with try + assert + except
    Only takes alphanum and space
    Convert in morse using Global Dictionnary
    """
    try:
        if len(sys.argv) != 2:
            assert False, \
                "AssertionError: the arguments are bad"

        string = str(sys.argv[1])
        sys.stdout.flush()
        if not all(char.upper() in NESTED_MORSE for char in string):
            assert False, "AssertionError: the arguments are bad"

        morse_code = ' '.join(NESTED_MORSE[char.upper()] for char in string)
        print(morse_code)


    except AssertionError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()