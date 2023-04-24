====================
Linear Extrapolation
====================

As the data is being built up, linear extrapolation is the most meaningful
method to predict whereabouts the next point should be. If several points of
data are present then linear extrapolation becomes one of several methods
that can be used. If the points do not lie on a straight line then, assuming
that the data should be on a straight line, use linear regression.

Provided there are at least two points project the line so that the new 
x-value gives the required y-value. Starting from the linear interpolation
equation (1.1), the inverse is:-

.. math::
    x = x_0 + \frac {(y - y_0)(x_1 - x_0)}{(y_1 - y_0)}     \tag{2.1}

The variables :math:`x_0, y_0, x_1\, and\, y_1` are known from the first two
evaluations of the function, so y will be the target value we wish to achieve,
and x is the required input to achieve this target. If the preliminary points
are close to the goal, or the underlying function is linear, then linear 
extrapolation may be all that is required. If we are starting to build up
the data then the first extrapolated point has to be linear extrapolation.


