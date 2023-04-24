# https://nickcdryan.com/2017/09/13/root-finding-algorithms-in-python-line-search-bisection-secant-newton-raphson-boydens-inverse-quadratic-interpolation-brents/
# https://blogs.mathworks.com/cleve/2015/10/12/zeroin-part-1-dekkers-algorithm/

from prettytable import PrettyTable

x = PrettyTable(['step', 'x0', 'x1', 'x2', 'f(x0)', 'f(x1)', 'f(x2)', 'tol'])

def inverse_quadratic_interpolation(f, x0, x1, x2, fx0, fx1, fx2, max_iter=20, tolerance=1e-5):
    steps_taken = 0
    while steps_taken < max_iter and abs(x1-x0) > tolerance: # last guess and new guess are v close
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
        new = L0 + L1 + L2

        x2, x0, x1 = x0, x1, new
        fx2, fx0, fx1 = fx0, fx1, f(new)

        steps_taken += 1
        x.add_row([steps_taken, round(x0,7), round(x1,7), round(x2,7), \
            round(fx0,7), round(fx1,7), round(fx2,7), round(abs(x1 - x0),7)])

    return x1, steps_taken

f = lambda x: x**3 + x**2 - 3*x - 3

X0 = -2#10 #-2 #2 #2
X1 = -4#12 #-4 #2.5 #1.75
X2 = -6#14 #-6 #3 #1.5
F0 = f(X0)
F1 = f(X1)
F2 = f(X2)


x.add_row([0, X0, X1, X2, F0, F1, F2, abs(X1 - X0)])
root, steps = inverse_quadratic_interpolation(f, x0=X0, x1=X1, x2=X2, \
                fx0=F0, fx1=F1, fx2=F2)

print(x)
print (f"root is: {root:.7}")
print ("steps taken:", steps)

'''
+------+-----------+-----------+----------+------------+------------+------------+-----------+
| step |     x0    |     x1    |    x2    |   f(x0)    |   f(x1)    |   f(x2)    |    tol    |
+------+-----------+-----------+----------+------------+------------+------------+-----------+
|  0   |    1.5    |    1.75   |    2     |   -1.875   |  0.171875  |     3      |    0.25   |
|  1   |  1.731238 |    1.5    |   1.75   | -0.0076882 |   -1.875   |  0.171875  |  0.231238 |
|  2   | 1.7320538 |  1.731238 |   1.5    |  2.86e-05  | -0.0076882 |   -1.875   | 0.0008158 |
|  3   | 1.7320508 | 1.7320538 | 1.731238 |    0.0     |  2.86e-05  | -0.0076882 |   3e-06   |
+------+-----------+-----------+----------+------------+------------+------------+-----------+
root is: 1.7320508080841999
steps taken: 3
'''