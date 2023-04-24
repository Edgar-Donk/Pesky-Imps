====================
Extrema Introduction
====================

If the original equation can be differentiated, one can readily extend root 
finding to maxima and minima. A positive second differential is a minimum
and a negative one is the maximum. If the original equation cannot be
differentiated then by adapting some of the numerical methods for root finding  
extrema can also be found, but the result of the test is not quite so clear 
cut. 

Checking that the limits straddle the point of interest will involve a few 
calculations. If our limits straddle the minimum then points between will 
have lower function evaluations, in which case the limits do straddle 
the minimum. If the one of the limit's value is lower than our test point
value then new limits are required.

Just as with root finding it is assumed that when the function is complicated
numerical methods will be necessary. In general
a bracketing procedure is more appropriate than the secant method. When
adding new intermediate points and changing the limits it may not be too 
obvious that the new limits still bracket the 
solution or are wandering off course. Adding additional tests will help but
increase the amount of work and slow down the process.

Bracketing
==========

Before optimising one needs to know roughly where a local maximum or minimum
lies. This is not as easy as root finding, especially if there is difficulty
in finding the first differential. We know that close to the point of interest
that given three equidistant starting points arranged in ascending order 
(x0 < x1 < x2) and :math:`x1 = (x0 + x2)/2`,
then if f(x0) > f(x1) and f(x2) > f(x1) the inner point has a value lower than
the values either side there must be a local minimum between x0 and x2, 
conversely if the inner point has a higher value than the values either
side there must be a local maximum between x0 and x2. 

Not all methods are self correcting, apart from using the given limits, check
what happens when the limits are changed. Also remember that other 
functions may interact differently with the various methods.

Example for Methods
===================

Finding extrema helps in solving and plotting equations, but probably more
importantly it can help in finding real life solutions. Say we have a cylinder
with closed ends, given the cylinder dimensions we can write the volume.

.. math::

    V = \pi \cdot r^2 \cdot l  \tag{1}

.. math::
    l = \frac {V}{\pi \cdot r^2}  \tag{2}

Say now we have a given volume and the ratio of length to radius we can
find required dimensions by substituting the length in the ratio in equation
(1). If we wish to reduce the amount of material used then we need to know 
the area of the cylinder with flat sides.

.. math::

    A = 2 \cdot \pi \cdot r^2 + 2 \cdot \pi \cdot r \cdot l  \tag{3} 

.. math::
    A = 2 \cdot \pi \cdot r^2 + \frac {2 \cdot \pi \cdot r \cdot V}{\pi \cdot r^2} 

.. math::
    A = 2 \cdot \pi \cdot r^2 + \frac {2 \cdot V}{r}  \tag{4}

Substituting the length from equation (2) into the area equation (3), after
simplifying we arrive at equation (4) which is used as the example
to find the minima.
