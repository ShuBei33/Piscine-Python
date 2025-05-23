from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Computes one or more statistical metrics based on keyword requests.

    Valid operations (passed as **kwargs values) are:
    - "mean": arithmetic average
    - "median": middle value in sorted data
    - "quartile": 25% and 75% percentiles
    - "std": standard deviation
    - "var": variance

    Args:
        *args: A variable number of numerical values (int or float).
        **kwargs: Any number of keyword arguments. Their values must be
        one of the valid operation names above.

    Returns:
        None: Prints results directly. If the operation is unknown, or if
        args are missing or invalid, prints "ERROR".
    """
    try:
        for val in kwargs.values():
            length = len(args)
            if length == 0:
                # No data provided → print error
                print("ERROR")
                continue

            # Sort the input values once for consistent indexing
            sort = sorted(args)

            if val == "mean":
                # Arithmetic mean: sum divided by number of elements
                mean = sum(sort) / length
                print(f"mean : {mean}")

            elif val == "median":
                # Median: mid value if odd, average of two mid val if even
                mid = length // 2
                if length % 2 == 0:
                    # Even → average of two center elements
                    median = (sort[mid - 1] + sort[mid]) / 2
                else:
                    # Odd → center element
                    median = sort[mid]
                print(f"median : {median}")

            elif val == "quartile":
                # Quartiles: 25% and 75% positions
                q1_index = int(0.25 * length)
                q3_index = int(0.75 * length)
                q1 = float(sort[q1_index])
                q3 = float(sort[q3_index])
                print(f"quartile : [{q1}, {q3}]")

            elif val == "var" or val == "std":
                # Compute the mean once
                mean = sum(sort) / length
                # Compute the variance (sum of squared diffs)
                squared_diffs = [(x - mean) ** 2 for x in sort]
                variance = sum(squared_diffs) / length

                if val == "var":
                    print(f"var : {variance}")
                else:
                    std_dev = variance ** 0.5
                    print(f"std : {std_dev}")

    except Exception as e:
        print(f"ERROR: {e}")
