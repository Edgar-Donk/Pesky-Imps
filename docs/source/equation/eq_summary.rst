====================
Summary Root Finding
====================

Which method should be used for root finding, depends on the application.

* Defining Limits

    Interval halving, linear interpolation and secant work best when the root is bracketed.

* Defining the Derivative

    The Newton-Raphson requires the derivative, or a good approximation, if the original function is spikey this may be impossible.

* Defining the Function Type

    Test the required method on a similar function.

Richard Brent used several sample functions in his testing of Brent's method,
select the type that is closest to your application to see which method works
best.

.. math::
    f(x)&=sin(x) - x/2 \\
    f(x)&=2 x -e^{-x} \\
    f(x)&=x e^{-x} \\
    f(x)&=e^x - \frac{1}{(100 x x)} \\
    f(x)&=(x + 3)(x - 1)(x - 1) \\
    f(x)&=\frac {e^x}{cos(x)} \\
    f(x)&=\frac {1}{(1 + 16 x^2)} 

The following functions were used by Matlab to test optimisation, so there 
may be roots here and there.

.. math::
    f(x)&= e^{-2 x} + x^2 \\
    f(x)&= -2 e^{-\sqrt x} (\sqrt x + 1) + cos(x) \\
    f(x)&= \frac {1}{720}(x^6-36x^5+450x^4-2400x^3+5400x^2-4320x+720) \\
    f(x)&= \frac {1}{\Gamma (x)} \\
    f(x)&= 64x^7 - 112x^5 + 56x^3 - 7x \\
    f(x)&= x(log(x)-1) - sin(x) \\
    f(x)&= -x + e^{-x} + xlog(x) \\
    f(x)&= -li(x)+xlog\,(log(x)) + cos(x) \\
    f(x)&= 1/2 \sqrt \pi\, erf(x) - x^3/3 \\
    f(x)&= 1/2 \sqrt \pi\, erf(x) - sin(x)

where :math:`\Gamma` is the Gamma function, li(x) is a logarithmic integral
and erf(x) is the error function

Choose a function we can program easily then use Scipy to help solve the 
root, and give the function fsolve an initial guess::

    from scipy.optimize import fsolve
    import numpy as np
    f = lambda x: np.sin(x) - x/2
    fsolve(f, [-10, 10])
    
    # array([0., 0.])

    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    sns.set_theme()
    
    f = lambda x: np.sin(x) - x/2
    
    xx = np.linspace(-2.5, 2.5)
    xx = np.linspace(-2.5, 2.5)
    yy = f(xx)
    plt.plot(xx, f(xx), 'c-', label='f(x')
    plt.hlines(0, -2.5, 2.5, 'g', label='x-axis')
    plt.legend()
    plt.title('Example Function for Root Finding\n$sin(x) - x/2$')
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    
    plt.show()

