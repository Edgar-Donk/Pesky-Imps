================================
Optimisation with Newton Raphson
================================

Root finding scripts can be used just by changing the testing method,
the newton raphson method for root finding remains unchanged except that it 
is used on the first derivative instead of the original function which means 
that the second derivative replaces the first derivative in root finding. If
the first derivative can be found it generally is better to use the newton 
raphson method straight away. 

Using the following script, which uses both the first and second derivatives,
the following results::

    +------+-----------+-------------+-------------+------------+
    | step |     x0    |      df     |     d2f     |   error    |
    +------+-----------+-------------+-------------+------------+
    |  0   |     1     | -87.4336294 | 212.5663706 | -0.4113239 |
    |  1   | 1.4113239 | -32.4697385 |  83.7122749 | -0.3878731 |
    |  2   |  1.799197 |  -8.2823778 |  46.9058612 | -0.1765745 |
    |  3   | 1.9757715 |  -0.788624  |  38.4974066 | -0.0204851 |
    |  4   | 1.9962566 |  -0.0081486 |  37.7072757 | -0.0002161 |
    |  5   | 1.9964727 |    -9e-07   |  37.6991127 |    -0.0    |
    +------+-----------+-------------+-------------+------------+
    The approximate value of x is: 1.9964726889295161
    Made in 5 iterations

The answer was made in 5 iterations, and only required one starting point, 
in this case 1. If the starting point was 5 it required 6 iterations::

    +------+-----------+--------------+-------------+------------+
    | step |     x0    |      df      |     d2f     |   error    |
    +------+-----------+--------------+-------------+------------+
    |  0   |     5     |  58.8318531  |  14.1663706 | 4.1529235  |
    |  1   | 0.8470765 | -128.7206394 | 341.6164924 | -0.3767987 |
    |  2   | 1.2238752 | -51.3817768  | 121.6648252 | -0.4223224 |
    |  3   | 1.6461976 | -16.2140978  |  57.3979599 | -0.2824856 |
    |  4   | 1.9286832 |  -2.6464825  |  40.4434532 | -0.0654366 |
    |  5   | 1.9941198 |  -0.0888081  |  37.7881818 | -0.0023502 |
    |  6   | 1.9964699 |  -0.0001046  |  37.6992167 |  -2.8e-06  |
    +------+-----------+--------------+-------------+------------+
    The approximate value of x is: 1.9964699371211263
    Made in 6 iterations

.. container:: toggle

    .. container:: header

        *Show/Hide Code* newton_optimize.py

    .. literalinclude:: ../examples/opt/newton_optimize.py

Applying a Newton-Raphson method to a simple complex function, one obtains a 
fractal:-

.. figure:: ../figures/newton_fractal.png
    :width: 640
    :height: 480
    :align: center
    
    Fractal using :math:`z = x + i\cdot y`