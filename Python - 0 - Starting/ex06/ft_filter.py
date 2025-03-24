def ft_filter(fct, it):
    """
    Recode the filter() function in Pyhton
    filter(function or None, iterable) --> filter object
    """

    try:
        iterator = iter(it)
    except TypeError:
        raise TypeError(f"'{type(it).__name__}' object is not iterable")

    fct = bool if fct is None else fct

    return (i for i in it if fct(i))