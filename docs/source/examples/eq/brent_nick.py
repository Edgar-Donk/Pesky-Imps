# https://nickcdryan.com/2017/09/13/root-finding-algorithms-in-python-line-search-bisection-secant-newton-raphson-boydens-inverse-quadratic-interpolation-brents/

from prettytable import PrettyTable

t = PrettyTable(['step', 'x0', 'x1', 'x2', 'f(x0)', 'f(x1)', 'f(x2)', 'emax'])

def brents(f, x0, x1, fx0, fx1, max_iter=50, tolerance=1e-5):

    assert (fx0 * fx1) <= 0, "Root not bracketed"

    if abs(fx0) < abs(fx1):
        x0, x1 = x1, x0

    x2 = x0

    mflag = True
    steps_taken = 0

    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        t.add_row([steps_taken, round(x0,7), round(x1,7), round(x2,7),\
            round(fx0,7), round(fx1,7), round(fx2,7), round(abs(x1-x0),7)])

        if fx0 != fx2 and fx1 != fx2:
            L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
            L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
            L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
            new = L0 + L1 + L2

        else:
            new = x1 - ( (fx1 * (x1 - x0)) / (fx1 - fx0) )

        if ((new < ((3 * x0 + x1) / 4) or new > x1) or
            (mflag == True and (abs(new - x1)) >= (abs(x1 - x2) / 2)) or
            (mflag == False and (abs(new - x1)) >= (abs(x2 - d) / 2)) or
            (mflag == True and (abs(x1 - x2)) < tolerance) or
            (mflag == False and (abs(x2 - d)) < tolerance)):
            new = (x0 + x1) / 2
            mflag = True

        else:
            mflag = False

        fnew = f(new)
        d, x2 = x2, x1

        if (fx0 * fnew) < 0:
            x1 = new
        else:
            x0 = new

        if abs(fx0) < abs(fx1):
            x0, x1 = x1, x0

        steps_taken += 1

    return x1, steps_taken


f = lambda x:  x**3 + x**2 - 3*x - 3

X0 = 2
X1 = 1.5

root, steps = brents(f, x0=X0, x1=X1, fx0=f(X0), fx1=f(X1), tolerance=1e-5)
print(t)
print ("root is:", root)
print ("steps taken:", steps-1)

'''
+------+-----------+-----------+-----------+------------+-----------+-----------+-----------+
| step |     x0    |     x1    |     x2    |   f(x0)    |   f(x1)   |   f(x2)   |    emax   |
+------+-----------+-----------+-----------+------------+-----------+-----------+-----------+
|  0   |     2     |    1.5    |     2     |     3      |   -1.875  |     3     |    0.5    |
|  1   |    1.75   |    1.5    |    1.5    |  0.171875  |   -1.875  |   -1.875  |    0.25   |
|  2   |   1.625   |    1.75   |    1.5    | -0.9433594 |  0.171875 |   -1.875  |   0.125   |
|  3   |   1.625   | 1.7324852 |    1.75   | -0.9433594 | 0.0041123 |  0.171875 | 0.1074852 |
|  4   | 1.7320501 | 1.7324852 | 1.7324852 |  -6.4e-06  | 0.0041123 | 0.0041123 | 0.0004351 |
|  5   | 1.7322677 | 1.7320501 | 1.7324852 | 0.0020527  |  -6.4e-06 | 0.0041123 | 0.0002175 |
|  6   | 1.7321589 | 1.7320501 | 1.7320501 | 0.0010231  |  -6.4e-06 |  -6.4e-06 | 0.0001088 |
|  7   | 1.7321045 | 1.7320501 | 1.7320501 | 0.0005084  |  -6.4e-06 |  -6.4e-06 |  5.44e-05 |
|  8   | 1.7320773 | 1.7320501 | 1.7320501 |  0.000251  |  -6.4e-06 |  -6.4e-06 |  2.72e-05 |
|  9   | 1.7320637 | 1.7320501 | 1.7320501 | 0.0001223  |  -6.4e-06 |  -6.4e-06 |  1.36e-05 |
+------+-----------+-----------+-----------+------------+-----------+-----------+-----------+
root is: 1.7320501357894793
steps taken: 9
'''