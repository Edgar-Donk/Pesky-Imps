=================
Linear Regression
=================

Linear regression or least squares regression line, chooses the line with
the least distance of the data points from the line. So that positive and
negative distances do not cancel each other out the distance is calculated
as a square. This makes outlyers more important than they should be. The
distance calculated is the vertical distance from the point to the line (both
at the same x-value), and not the perpendicular distance to the point. The
total effect of several points to the line:-

.. math::
    \hat y = mx + c

is:-

.. math::
    m &= \frac {n \sum(xy) - \sum x \sum y}{n \sum(x^2) - (\sum x)^2} \\
    c &= \frac {\sum y - m \sum x}{n}

where n is the number of points.

This method is applied to several points, so when starting to create data
first use linear extrapolation (2 points), then quadratic interpolation
(3 points) thereafter linear regression. It is assumed that the various
modes of the linear regression will enable a forecast of the next point once 
the equation of the regression has been found.

After the line has been fitted one should check whether it is a good fit or 
not. The difference between the actual y-value and the estimated y_value at 
the same x-value is the **residual**. If the linear regression has a good fit
then residuals will be scattered above and below the linear regression line.
As they stand if the residuals are added together then all the values will
cancel each other out, so use R-squared which evaluates the scatter of the 
points around the line, so a high
value, almost 100%, is generally what we want. If the fit has residuals
consistently on one side or the other and not scattered at random, then the 
data is biased and the fit needs correcting.

.. math::
    R^2 = \frac {Variance\, explained\, by\, the\, model}{Total\, Variance}

When in Python we are a bit spoilt for choice numpy, scipy, statsmodels,
sklearn and others. Use the one that suits the application best. Here's one 
to add to the mix, use it to see how the linear regression works rather than
use for major applications. From `Regression <https://web.stanford.edu/class/stats191/markdown/Chapter7/Simple_Linear_Regression.html>`_
and `Inference <https://web.stanford.edu/class/archive/cs/cs109/cs109.1218/files/student_drive/8.1.pdf>`_

.. container:: toggle

    .. container:: header

        *Show/Hide Code* custom_linear_regression.py

    .. literalinclude:: ../examples/extrap/custom_linear_regression.py

As an example see how using :math:`x = np.linspace(0, 1, 101)` and 
:math:`y = 1 + x + x * np.random.random(len(x))`, which should give m=1.5 and 
c=1.0 based on this data using numpy **polyfit** and **Polynomial**. For a 
linear fit use polyfit(x, y, 1). 

.. container:: toggle

    .. container:: header

        *Show/Hide Code* lin_regress_P_numpy.py

    .. literalinclude:: ../examples/extrap/lin_regress_P_numpy.py

The original script used numpy **linalg.lstsq** to create the linear 
regression function.

At present there are two polyfit modules, the older
version is np.polyfit that uses :math:`ax^3 + bx^2 + cx +d`, and a newer
version np.polynomial.polynomial.polyfit that uses the function in the 
reversed order :math:`d + cx + bx^2 + ax^3`. The latter ought to be used, 
but most websites still use the older version.

.. exec_code::

    import numpy as np
    p1d = np.poly1d([1, 2, 3])
    print('old format p1d:\n',p1d)
    
    p = np.polynomial.Polynomial(p1d.coef[::-1]) # coefficients flipped
    print('new format p:',p)

The polynomial package shows the coefficients also have domain and window 
attributes. The new polyfit can only be used for standard linear regression, 
whereas *fit* can be used with other fitting techniques.

Numpy advises using **fit** in the new version, the coefficients
are given in the *scaled domain* defined by the linear mapping between the 
window and domain, to get coefficients in the unscaled domain use **convert()**.
The domain is the interval [domain[0], domain[1]] mapped to the interval
[window[0], window[1]] by shifting and scaling. Both domain and window have 
default values [-1, 1].

.. exec_code::

    import numpy as np
    rng = np.random.default_rng()
    x = np.arange(10)
    y = np.arange(10) + rng.standard_normal(10)
    old = np.polyfit(x, y, deg=1)
    print('old format polyfit:', old) 
    p_fitted = np.polynomial.Polynomial.fit(x, y, deg=1)
    print('new format p_fitted:',p_fitted)
    print('p_fitted.convert():',p_fitted.convert())
    pf = np.polynomial.polynomial.polyfit(x, y, deg=1)
    print('new format polyfit pf:',pf)

Visualisation
=============

It is usual to plot the outcome to see how the regression worked out, in 
which case one could use Seaborn directly, but they advise using the
statsmodel to show the information. One can alter Seaborn's confidence interval
by changing the attribute **ci** for both lineplot and regplot.

After checking the outcome on a plot,
a second plot should be used, this plots residuals against the x-values. The
residuals should lie evenly spread close to the mean, in a random manner 
showing no trend. 

Other Models
============

The least squares method can be adapted to functions other than just the 
straight line. 

Exponential Functions
---------------------

In numpy say we have an exponential function :math:`ŷ(x) = \alpha e^{\beta x}`
take log on both sides :math:`log(ŷ(x)) = log(\alpha) + \beta x`

.. container:: toggle

    .. container:: header

        *Show/Hide Code* exp_regress_P_numpy.py

    .. literalinclude:: ../examples/extrap/exp_regress_P_numpy.py

Arrhenuis Equation
------------------

The solution for the Arrhenuis equation can be treated as for an exponential
function, so by taking logs on both sides:

.. math:: 
    k &= Ae^{-E_a/RT} \\
    ln\, k &= ln\, A - \frac {E_a}{R} \frac {1}{T} 

.. math::
    ln\, k = -\frac {E_a}{R} \left( \frac {1}{T} \right) +ln\, A \tag 1

where:

* k rate constant

* T absolute temperature, K

* A pre-exponential factor

* :math:`E_a` activation energy

* R universal gas constant

The last equation (1) treats the reciprocal temperature as the x variable
in a straight line equation :math:`y = m\,x + c`.

Simple Power
------------

A similar process used for exponential functions can be used on simple power 
expressions.
So a function :math:`ŷ(x) = b\, x^m` can be turned into a linear form by
taking logs on both sides :math:`log(ŷ(x)) = m\, log(x) + log\, b`.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* power_regress_P_numpy.py

    .. literalinclude:: ../examples/extrap/power_regress_P_numpy.py

Polynomial
----------

If the underlying function is a polynomial then the simplest numpy functions
to use is *y_est = poly.polyfit(x, y, j)* where x and y are data
numpy arrays, and j is the polynomial order. Assuming that a larger number of
x-values will be required for plotting, *x_new*, plot use 
*x_new, np.polyval(x_new, y_est)* for the x and y values. 

When deciding which polynomial fits best remember to set the attribute **full**
to True. The term that follows immediately after the coefficient array is the
residuals array, which is the sum of squared residuals of the least squares 
fit.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* numpy_P_4deg.py

    .. literalinclude:: ../examples/extrap/numpy_P_4deg.py

On Seaborn add the attribute **order** with the polynomial 
order for non-linear plots. If an outlyer ruins the regression line use
**robust=True** then the outlyer is ignored.

