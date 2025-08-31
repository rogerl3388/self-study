def twenty_twenty_three():
    """Come up with the most creative expression that evaluates to 2023,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_three()
    2023
    """
    return int((2**1)*10**3 + 96*(8+3-11) + 23 )

if __name__ == "__main__":
    import doctest
    doctest.testmod()