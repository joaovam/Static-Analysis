from lang import *


def test_min(m, n):
    """
    Stores in the variable 'answer' the minimum of 'm' and 'n'

    Examples:
        >>> test_min(3, 4)
        3
        >>> test_min(4, 3)
        3
    """
    env = Env({"m": m, "n": n, "x": m, "zero": 0})
    m_min = Add("answer", "m", "zero")
    n_min = Add("answer", "n", "zero")
    p = Lth("p", "n", "m")
    b = Bt("p", n_min, m_min)
    p.add_next(b)
    interp(p, env)
    return env.get("answer")


def test_fib(n):
    """
    Stores in the variable 'answer' the n-th number of the Fibonacci sequence.

    Examples:
        >>> test_fib(2)
        2
        >>> test_fib(3)
        3
        >>> test_fib(6)
        13
    """
    env = Env({"c": 0, "N": n, "fib0": 0, "fib1": 1, "zero": 0, "one": 1})
    i0 = Lth("p", "c", "N")
    i2 = Add("aux", "fib1", "zero")
    i3 = Add("fib1", "aux", "fib0")
    i4 = Add("fib0", "aux", "zero")
    i5 = Add("c", "c", "one")
    i6 = Add("answer", "fib1", "zero")
    i1 = Bt("p", i2, i6)
    i0.add_next(i1)
    i2.add_next(i3)
    i3.add_next(i4)
    i4.add_next(i5)
    i5.add_next(i0)
    interp(i0, env)
    return env.get("answer")


def test_min3(x, y, z):
    """
    Stores in the variable 'answer' the minimum of 'x', 'y' and 'z'

    Examples:
        >>> test_min3(3, 4, 5)
        3
        >>> test_min3(5, 4, 3)
        3
    """
    # TODO: Implement this method
    env = Env({"x":x, "y":y, "z":z, "zero":0 })

    x_min = Add("answer", "x", "zero")
    y_min = Add("answer", "y", "zero")
    z_min = Add("answer", "z", "zero")
    
    p1 = Lth("p","x", "y")

    p2 = Lth("p", "x", "z")
    x_or_z = Bt("p", x_min, z_min)
    
    p3 = Lth("p", "y", "z")
    y_or_z = Bt("p", y_min, z_min)

    i0 = Bt("p", p2, p3)

    p1.add_next(i0)
    p2.add_next(x_or_z)
    p3.add_next(y_or_z)

    interp(p1, env)

    return env.get("answer")


def test_div(m, n):
    """
    Stores in the variable 'answer' the integer division of 'm' and 'n'.

    Examples:
        >>> test_div(30, 4)
        7
        >>> test_div(4, 3)
        1
        >>> test_div(1, 3)
        0
    """
    env = Env({"m":m, "n":n, "zero": 0, "one":1, "count":0, "x":n})# 10/3 -> 3 6 9
    
    ret_count = Add("answer", "count", "zero")

    init_division = Lth("p", "x", "m")
    i1 = Add("x", "x", "n")

    i0 = Bt("p", i1 ,ret_count)

    i2 = Add("count", "count", "one")
    
     # primeiro teste

    n_is_zero = Bt("n", init_division ,ret_count)#OK
    m_is_zero = Bt("m", n_is_zero ,ret_count)#OK

    i2.add_next(init_division)
    i1.add_next(i2)
    init_division.add_next(i0)
    

    interp(m_is_zero, env)

    return env.get("answer")


def test_fact(n):
    """
    Stores in the variable 'answer' the factorial of 'n'.

    Examples:
        >>> test_fact(3)
        6
    """
    # TODO: Implement this method

    #fact = 5 * 4 * 3 * 2 * 1
    env = Env({"zero": 0, "one":1, "x":2,"count":1, "minus_1": -1, "n":n, "fact":1})

    finish = Add("answer", "fact", "zero")

    i1 = Geq("p", "count", "n")
    fact = Mul("fact", "fact", "x")
    i3 = Add("x", "x", "one")
    i4 = Add("count", "count", "one")
    i0 = Bt("p", finish, fact)

    fact.add_next(i3)
    i3.add_next(i4)
    i4.add_next(i1)
    i1.add_next(i0)

    interp(i1, env)
    return env.get("answer")
