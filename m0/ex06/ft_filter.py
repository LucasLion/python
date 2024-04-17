def ft_filter(func, it):
    """filter(function or None, iterable) --> filter object\n
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    if func:
        return (i for i in it if func(i))
    return (i for i in it if func)
