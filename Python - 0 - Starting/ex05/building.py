import sys

def main():
    """
    Catch errors with try + assert + except
    Count upper-case char, lower-case char, \
    punctuation char, digits, spaces and total char
    Displays it as requested
    """


    try:
        if len(sys.argv) > 2:
            assert False, \
                "AssertionError: more than one argument is provided"
        elif len(sys.argv) == 1:
            print("What is the text to count?", flush=True)
            str = sys.stdin.read()
        else:
            str = sys.argv[1]


        upper_cnt = 0
        lower_cnt = 0
        digit_cnt = 0
        space_cnt = 0
        punct_cnt = 0
        space_chars = " \t\n\r\v\f"


        for char in str:
            if 'A' <= char <= 'Z':
                upper_cnt += 1
            elif 'a' <= char <= 'z':
                lower_cnt += 1
            elif '0' <= char <= '9':
                digit_cnt += 1
            elif char in space_chars:
                space_cnt += 1
            else:
                punct_cnt += 1


        print(f"The text contains {len(str)} characters:")
        print(f"{upper_cnt} upper letters")
        print(f"{lower_cnt} lower letters")
        print(f"{punct_cnt} punctuation marks")
        print(f"{space_cnt} spaces")
        print(f"{digit_cnt} digits")


    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()