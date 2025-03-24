import sys

try:
    if len(sys.argv) < 2:
        assert False, "AssertionError: no argument is provided"
    elif len(sys.argv) > 2:
        assert False, "AssertionError: more than one argument is provided"

    try:
        nb = int(sys.argv[1])
    except ValueError:
        assert False, "AssertionError: argument is not an integer"
    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(e)
    sys.exit(1)