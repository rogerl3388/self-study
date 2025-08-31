def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    fall_output = 1
    while k > 0:
        fall_output = fall_output * n
        n -= 1
        k -= 1
    return fall_output


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    count, test_value = 0, 1
    while test_value <= n:
        if test_value % k == 0:
            count += 1
            print(test_value)
        test_value += 1
    return count


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    if y < 10:
        total_sum = y
    else:
        total_sum = sum_digits(y//10) + y % 10
    return total_sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    n = str(n)
    thing = False
    if len(n) > 1:
        i = 0
        while i < len(n) - 1:
            if n[i] == "8" and n[i+1] == "8":
                thing = True
                break
            i += 1
    return thing


if __name__ == "__main__":
    import doctest
    doctest.testmod()