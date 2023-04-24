=============
Secant Method
=============

The secant method improves the selection of the two values carried forward
for recalcuation. Instead of requiring that the function values for the 
calculated and one of the previous values be of opposite sign (as used in
linear interpolation), select the two function values closest to the final
root. The calculated value for the first interpolation is similar to that
used by linear inerpolation, but the new values are simply made by 
successively updating the old values.

One advantage of this method is that if the root has not been bracketed, it
should still find the root, albeit with more iterations. If one knows the
closest guess to the root, place this in the **b** position and the other guess 
in the **a** position, and the number of iterations should be reduced.

Using the same polynomial as before.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* secant_nick.py

    .. literalinclude:: ../examples/eq/secant_nick.py

which resulted in::

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
    root is:1.732051 in 5 interpolations

and by swapping the input guesses::

    +------+-----------+-----------+-----------+------------+------------+------------+-----------+
    | step |     a     |     b     |     x1    |    f(a)    |    f(b)    |   f(x1)    |   |b-a|   |
    +------+-----------+-----------+-----------+------------+------------+------------+-----------+
    |  0   |     2     |    1.5    |    None   |     3      |   -1.875   |    None    |   1e-05   |
    |  1   |    1.5    | 1.6923077 | 1.6923077 |   -1.875   | -0.3664087 | -0.3664087 | 0.1923077 |
    |  2   | 1.6923077 | 1.7390157 | 1.7390157 | -0.3664087 | 0.0662169  | 0.0662169  |  0.046708 |
    |  3   | 1.7390157 | 1.7318666 | 1.7318666 | 0.0662169  | -0.001743  | -0.001743  |  0.007149 |
    |  4   | 1.7318666 |  1.73205  |  1.73205  | -0.001743  |  -7.9e-06  |  -7.9e-06  | 0.0001834 |
    |  5   |  1.73205  | 1.7320508 | 1.7320508 |  -7.9e-06  |    0.0     |    0.0     |   8e-07   |
    +------+-----------+-----------+-----------+------------+------------+------------+-----------+
    root is:1.732051 in 5 interpolations