def even_weighted_loop(s: list) -> list:
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    # result: list = []
    # for i, n in enumerate(s):
    #     if i % 2 == 0:
    #         result.append(i * n)
    # return result
    return [i * n for i,n in enumerate(s) if i % 2 == 0]

def max_product(s: list) -> list:
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([1,5,1,1,9,1,10,1]) # 5 * 9 * 10
    450
    >>> max_product([])
    1
    """
    if len(s) < 1:
        return 1
    if len(s) == 1:
        return s[0]
    return max([s[0] * max_product(s[2:]), s[0] * max_product(s[3:]),s[1] * max_product(s[3:]),s[1] * max_product(s[4:])])


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()