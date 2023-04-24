# https://nickcdryan.com/2017/09/13/root-finding-algorithms-in-python-line-search-bisection-secant-newton-raphson-boydens-inverse-quadratic-interpolation-brents/

from prettytable import PrettyTable

x = PrettyTable(['step', 'a', 'b', 'x1', 'f(a)', 'f(b)', 'f(x1)', '|b-a|'])

def secant_method(f, a, b, fa, fb, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    while steps_taken < max_iter and abs(b-a) > tolerance:
        x1 = b - ( (fb * (b - a)) / (fb - fa) )
        f1 = f(x1)
        b, a = x1, b
        fb, fa = f1, fb
        x.add_row([steps_taken, round(a,7), round(b,7), round(x1,7),\
            round(fa,7), round(fb,7), round(f1,7), round(abs(b-a),7)])
        steps_taken += 1
    return x1, steps_taken-1

f = lambda x: x**3 + x**2 - 3*x - 3

A = 1.5
B = 2
FA = f(A)
FB = f(B)
x.add_row([0, A, B, None, FA, FB, None, 1e-5])
root, steps = secant_method(f, a=A, b=B, fa=FA, fb=FB)
print(x)
print (f"root is: {root:.7} in {steps} interpolations")

'''
+------+-----------+-----------+-----------+------------+------------+------------+-----------+
| step |     a     |     b     |     x1    |    f(a)    |    f(b)    |   f(x1)    |   |b-a|   |
+------+-----------+-----------+-----------+------------+------------+------------+-----------+
|  0   |    1.5    |     2     |    None   |   -1.875   |     3      |    None    |   1e-05   |
|  1   |     2     | 1.6923077 | 1.6923077 |     3      | -0.3664087 | -0.3664087 | 0.3076923 |
|  2   | 1.6923077 | 1.7257977 | 1.7257977 | -0.3664087 | -0.0589377 | -0.0589377 |  0.03349  |
|  3   | 1.7257977 | 1.7322173 | 1.7322173 | -0.0589377 | 0.0015757  | 0.0015757  | 0.0064196 |
|  4   | 1.7322173 | 1.7320501 | 1.7320501 | 0.0015757  |  -6.5e-06  |  -6.5e-06  | 0.0001672 |
|  5   | 1.7320501 | 1.7320508 | 1.7320508 |  -6.5e-06  |    -0.0    |    -0.0    |   7e-07   |
+------+-----------+-----------+-----------+------------+------------+------------+-----------+
root is: 1.7320508074943775
steps taken: 5
'''