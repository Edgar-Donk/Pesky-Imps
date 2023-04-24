# https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html

# NEW VERSION #

import numpy as np
from numpy.polynomial import polynomial as P

np.random.seed(123)

x = np.linspace(-1,1,51) # x "data": [-1, -0.96, ..., 0.96, 1]

y = x**3 - x + np.random.randn(len(x))  # x^3 - x + Gaussian noise

c, stats = P.polyfit(x,y,3,full=True)

np.random.seed(123)

'''
c # c[0], c[2] should be approx. 0, c[1] approx. -1, c[3] approx. 1
array([ 0.01909725, -1.30598256, -0.00577963,  1.02644286]) # may vary

# SSR first term stats
stats # note the large SSR, explaining the rather poor results
 [array([ 38.06116253]), 4, array([ 1.38446749,  1.32119158,  0.50443316, # may vary
          0.28853036]), 1.1324274851176597e-014]
'''
# Same thing without the added noise

y = x**3 - x

c, stats = P.polyfit(x,y,3,full=True)

'''
c # c[0], c[2] should be "very close to 0", c[1] ~= -1, c[3] ~= 1
array([-6.36925336e-18, -1.00000000e+00, -4.08053781e-16,  1.00000000e+00])

    stats # note the minuscule SSR
    [array([  7.46346754e-31]), 4, array([ 1.38446749,  1.32119158, # may vary
               0.50443316,  0.28853036]), 1.1324274851176597e-014]

'''