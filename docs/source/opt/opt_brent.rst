
Minimum with Brent
==================

Brent's method can be used to find minima, as with root finding it involves
a slow but sure algorithm as well as a fast algorithm. The limits are updated
to try and avoid a situation where the result could flip between two values.
Part of this routine uses a parabola to find a better position based on its
minimum. So a quadratic parabola is drawn through the two limits and a computed
point in between, provided the three ponts are not colinear compute a parabola
:math:`a\cdot x² + b \cdot x + c`, the minimum of which is located at
:math:`x = - \frac {b} {2 \cdot a}`. With each iteration reuse the last 
computed position as a new limit. The slow method is the golden ratio method.

Brent actually used a Lagrange polynomial, which is summarised as p(x), with
its minimum at :math:`x_4`.

.. math::
    p(x) = \frac {(x - x_2)(x - x_3)}{(x_1 - x_2)(x_1 - x_3)} f(x_1) + \frac {(x - x_1)(x - x_3)}{(x_2 - x_1)(x_2 - x_3)} f(x_2) + \frac {(x - x_1)(x - x_2)}{(x_3 - x_1)(x_3 - x_2)} f(x_3)

.. math::
    x_4 = x_2 - 1/2 \frac {(x_2 - x_1)^2[f(x_2) - f(x_3)] - (x_2 - x_3)^2[f(x_2) - f(x_1)]} {(x_2 - x_1)[f(x_2) - f(x_3)] - (x_2 - x_3)[f(x_2) - f(x_1)]}

The thinking was that near to a minimum it resembles a parabola, which is
just what was used in the quadratic interpolation, except that in Brent's 
method, just as with root finding, there needs to be checks to ensure that
the interpolation is progressing::

    Wed Mar 22 13:45:16 2023
    
    LOCAL_MIN_TEST
    Python version: 3.10.4
    LOCAL_MIN seeks a local minimizer of a function F(X)
    
    g_01(x) = 2 (pi x^2 + 50 / x
    in an interval [A,B] [1,5].
    g_01(1.99647) = 75.1325
    +------+-----------+-----------+-----------+-----------+-----------+------------+-------------+-------------+-----------+----------+
    | step |     a     |     x     |     v     |     w     |     b     |    f(x)    |     f(v)    |     f(w)    |    emax   |  method  |
    +------+-----------+-----------+-----------+-----------+-----------+------------+-------------+-------------+-----------+----------+
    |  0   |     1     |  2.527864 |  2.527864 |  2.527864 |     5     | 79.7092508 |  79.7092508 |  79.7092508 |  0.472136 |   None   |
    |  1   |     1     |  2.527864 |  3.472136 |  2.527864 |  3.472136 | 79.7092508 | 104.5490892 |  79.7092508 |  0.472136 |   gold   |
    |  2   |     1     | 1.9442719 |  2.527864 |  3.472136 |  2.527864 | 75.1847899 |  79.7092508 | 104.5490892 | 0.2917961 |   gold   |
    |  3   | 1.9168427 | 1.9442719 | 1.9168427 |  2.527864 |  2.527864 | 75.1847899 |  75.2553409 |  79.7092508 | 0.1803399 | parabola |
    |  4   | 1.9442719 | 2.0066655 | 1.9442719 | 1.9168427 |  2.527864 | 75.1344587 |  75.1847899 |  75.2553409 | 0.2156879 | parabola |
    |  5   | 1.9442719 | 1.9959898 | 2.0066655 | 1.9442719 | 2.0066655 | 75.1325114 |  75.1344587 |  75.1847899 | 0.2400782 | parabola |
    |  6   | 1.9959898 | 1.9965588 | 1.9959898 | 2.0066655 | 2.0066655 | 75.1325071 |  75.1325114 |  75.1344587 | 0.0210901 | parabola |
    |  7   | 1.9959898 | 1.9964734 | 1.9965588 | 1.9959898 | 1.9965588 | 75.132507  |  75.1325071 |  75.1325114 | 0.0048543 | parabola |
    |  8   | 1.9959898 | 1.9964727 | 1.9964734 | 1.9965588 | 1.9964734 | 75.132507  |  75.132507  |  75.1325071 | 0.0001984 | parabola |
    |  9   | 1.9964725 | 1.9964727 | 1.9964725 | 1.9964734 | 1.9964734 | 75.132507  |  75.132507  |  75.132507  | 0.0002411 | parabola |
    |  10  | 1.9964725 | 1.9964727 | 1.9964725 | 1.9964729 | 1.9964729 | 75.132507  |  75.132507  |  75.132507  |   2e-07   | parabola |
    |  11  | 1.9964725 | 1.9964727 | 1.9964725 | 1.9964725 | 1.9964729 | 75.132507  |  75.132507  |  75.132507  |    0.0    |   gold   |
    +------+-----------+-----------+-----------+-----------+-----------+------------+-------------+-------------+-----------+----------+
    
    LOCAL_MIN_TEST
    Normal end of execution.
    Wed Mar 22 13:45:16 2023

This script was of several based on Richard Brent's work by John Burkhardt, 
the original script **local_min.py** included tests on 6 different functions.
This was modified to run on the test function, PrettyTable was added to view
the variables' progress and which method was used. Additional checks were
added to confirm that the limits bracketed a minimum. Some of the ancilliary
functions could be used to help with the output. 

.. container:: toggle

    .. container:: header

        *Show/Hide Code* local_min_rev1.py

    .. literalinclude:: ../examples/opt/local_min_rev1.py