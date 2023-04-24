import math


invphi = (math.sqrt(5) - 1) / 2  # 1 / phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1 / phi^2


def gssrec(f, a, b, tol=1e-5, h=None, x1=None, x2=None, F1=None, F2=None):
    """Golden-section search, recursive.

    Given a function f with a single local minimum in
    the interval [a,b], gss returns a subset interval
    [c,d] that contains the minimum with d-c <= tol.

    Example:
    >>> f = lambda x: (x-2)**2
    >>> a = 1
    >>> b = 5
    >>> tol = 1e-5
    >>> (c,d) = gssrec(f, a, b, tol)
    >>> print (c, d)
    1.9999959837979107 2.0000050911830893
    """

    (a, b) = (min(a, b), max(a, b))
    if h is None:
        h = b - a
    if h <= tol:
        return (a, b)
    if x1 is None:
        x1 = a + invphi2 * h
    if x2 is None:
        x2 = a + invphi * h
    if F1 is None:
        F1 = f(x1)
    if F2 is None:
        F2 = f(x2)
    if F1 < F2:  # F1 > F2 to find the maximum
        return gssrec(f, a, x2, tol, h * invphi, x1=None, F1=None, x2=x1, F2=F1)
    else:
        return gssrec(f, x1, b, tol, h * invphi, x1=x2, F1=F2, x2=None, F2=None)

f = lambda x: 2 * (math.pi*x**2 + 50/x) # (x-2)**2
a = 1
b = 5
tol = 1e-5
(c,d) = gssrec(f, a, b, tol)
print ("Minimum value of f(x) is", f((c+d)/2), "at x =", (c + d)/2)

