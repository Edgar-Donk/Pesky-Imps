==========================
Extrapolation Introduction
==========================

Extrapolation can be similar to interpolation if we assume that the function
behaves similarly to existing data. Since the next point has not yet been 
bracketed there is always the possibility that the behaviour changes, 
depending on the application. Simple extrapolation predicts existing data
to fit into the best model.

* Linear
    Used when data increases or decreases at a steady rate, or only two data points.

* Power
    Measurements increase at a specific rate, problems at zero and negative x-values.

* Quadratic
    Starting to build our data and fitting three points.

* Cubic Spline
    Similar to quadratic but using more prediction of how the function grows.

* Exponential
    Data changes at increasingly higher rates, and there are no negative or zero x-values.

* Logarithmic
    Data changes swiftly, there are no negative or zero x-values.

* Polynomial
    Can only be used with more data. Often used as an extension to other methods.

Without a well fitting model expect the results to be unpredicable. If the 
data is coming from field readings be aware of outliers.

.. figure:: ../figures/extrap_intro.png
    :width: 640
    :height: 480
    :align: center

    Comparing the results of fitting the least squares line and polynomial
    to the data.
    
    If the data should be linear then the projected point for an x-axis value
    of 2 is shown (green point), and the polynomial should be ignored.