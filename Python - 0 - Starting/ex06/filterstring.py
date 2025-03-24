import sys
from ft_filter import ft_filter

def len_filter(word, num):
    """
    Check if the word lenght is greater than num
    """
    return len(word) > num


def main():
    """
    Catch errors with try + assert + except
    Program needs a string and an integer and displays \
    a list of those which lenght is greater than the int given
    Use of ft_filter().
    Output is displayed between "[...]"
    """
    try:
        if len(sys.argv) != 3:
            assert False, \
                "AssertionError: the arguments are bad"

        string = str(sys.argv[1])
        sys.stdout.flush()
        if not all(char.isalpha() or char == " " for char in string):
            assert False, "AssertionError: the first argument is bad"
        try:
            integer = int(sys.argv[2])
        except ValueError:
            assert False, "AssertionError: the second argument is bad"

        words = [word for word in string.split() if word]

        #create anonymous function which takes every word
        filtered = ft_filter(lambda word: len_filter(word, integer), words)

        print(f"[{', '.join(filtered)}]")

    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()