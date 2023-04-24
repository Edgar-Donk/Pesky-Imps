#! /usr/bin/env python
#
import numpy as np
import platform
import time
from sys import exit
from prettytable import PrettyTable

pt = PrettyTable(['step', 'a', 'x', 'v', 'w', 'b', 'f(x)', 'f(v)', 'f(w)', 'emax', 'method'])

def g_01 ( x ):

#*****************************************************************************80
#
## G_01 evaluates 2 * (pi*x^2 + 50/x)
#
#  Discussion:
#
#    There is a local minimum between 1 and 15 at about
#    2.0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 March 2023
#
#  Author:
#
#    Edga Donk
#
#  Parameters:
#
#    Input, real X, the point at which F is to be evaluated.
#
#    Output, real VALUE, the value of the function at X.
#

    value = 2 * (np.pi * x * x + 50 / x)

    return value

def local_min ( a, b, epsi, t, f ):

#*****************************************************************************80
#
## LOCAL_MIN seeks a local minimum of a function F(X) in an interval [A,B].
#
#  Discussion:
#
#    The method used is a combination of golden section search and
#    successive parabolic interpolation.  Convergence is never much slower
#    than that for a Fibonacci search.  If F has a continuous second
#    derivative which is positive at the minimum (which is not at A or
#    B), then convergence is superlinear, and usually of the order of
#    about 1.324....
#
#    The values EPSI and T define a tolerance TOL = EPSI * abs ( X ) + T.
#    F is never evaluated at two points closer than TOL.
#
#    If F is a unimodal function and the computed values of F are always
#    unimodal when separated by at least SQEPS * abs ( X ) + (T/3), then
#    LOCAL_MIN approximates the abscissa of the global minimum of F on the
#    interval [A,B] with an error less than 3*SQEPS*abs(LOCAL_MIN)+T.
#
#    If F is not unimodal, then LOCAL_MIN may approximate a local, but
#    perhaps non-global, minimum to the same accuracy.
#
#    Thanks to Jonathan Eggleston for pointing out a correction to the
#    golden section step, 01 July 2013.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    Original FORTRAN77 version by Richard Brent.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization Without Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Parameters:
#
#    Input, real A, B, the endpoints of the interval.
#
#    Input, real EPSI, a positive relative error tolerance.
#    EPSI should be no smaller than twice the relative machine precision,
#    and preferably not much less than the square root of the relative
#    machine precision.
#
#    Input, real T, a positive absolute error tolerance.
#
#    Input, function value = F ( x ), the name of a user-supplied
#    function whose local minimum is being sought.
#
#    Output, real X, the estimated value of an abscissa
#    for which F attains a local minimum value in [A,B].
#
#    Output, real FX, the value F(X).
#
#
#  C is the square of the inverse of the golden ratio.
#
    if ( b == a ):

            print ( '' )
            print ( 'LOCAL_MIN_RC - Fatal error!' )
            print ( '  A < B is required, but' )
            print ( '  A = %f' % ( a ) )
            print ( '  B = %f' % ( b ) )
            status = -1
            exit ( 'LOCAL_MIN_RC - Fatal error!' )
    if a < b:
        pass
    else:
        a, b = b, a


    c = 0.5 * ( 3.0 - np.sqrt ( 5.0 ) )

    sa = a
    sb = b
    m = 0.5 * ( sa + sb )

    fa, fb, fm = f(a), f(b), f(m)
    #print('fa, fb, fm',fa, fb, fm)
    if fm < fa and fm < fb:
        pass
    else:

        print ( '' )
        print ( 'LOCAL_MIN_RC - Fatal error!' )
        print('Select new limits')
        print ( '  value a and value b > value mid point' )
        print ( f'  {a} has a value {fa}')
        print ( f'  {b} has a value {fb}')
        print ( f' mid point {m} has a value {fm}, should be less')
        status = -1
        exit ( 'LOCAL_MIN_RC - Fatal error!' )

    x = sa + c * ( b - a )
    w = x
    v = w
    e = 0.0  # Distance moved on the step before last
    fx = f ( x )
    fw = fx
    fv = fw
    tol = epsi * abs ( x ) + t
    t2 = 2.0 * tol
    step = 0
    pt.add_row([step, round(sa,7), round(x,7), round(w,7), round(v,7), round(sb,7), \
            round(fx,7), round(fw,7), round(fv,7), round(abs(x-m),7), None])

    while ( abs ( x - m ) > t2 - 0.5 * ( sb - sa ) ):

        m = 0.5 * ( sa + sb )
        tol = epsi * abs ( x ) + t
        t2 = 2.0 * tol
#
#  Fit a parabola.
#
        r = 0.0
        q = r
        p = q

        if ( tol < abs ( e ) ): #Construct a trial parabolic ﬁt.

            r = ( x - w ) * ( fx - fv )
            q = ( x - v ) * ( fx - fw )
            p = ( x - v ) * q - ( x - w ) * r
            q = 2.0 * ( q - r )

            p = -p if 0.0 < q else p

            q = abs ( q )

            r = e
            e = d

        if ( abs ( p ) < abs ( 0.5 * q * r ) and \
             q * ( sa - x ) < p and \
             p < q * ( sb - x ) ):
#
#  Take the parabolic interpolation step.
#
            d = p / q
            u = x + d
            method = 'parabola'
#
#  F must not be evaluated too close to A or B.
#
            if ( ( u - sa ) < t2 or ( sb - u ) < t2 ):

                if ( x < m ):
                    d = tol
                else:
                    d = - tol
#
#  A golden-section step.
#
        else:

            if ( x < m ):  # choose the larger of the two segments
                e = sb - x
            else:
                e = sa - x

            d = c * e
            method = 'gold'
#
#  F must not be evaluated too close to X.
#
        if ( tol <= abs ( d ) ):
            u = x + d
        elif ( 0.0 < d ):
            u = x + tol
        else:
            u = x - tol

        fu = f ( u )  # the one function evaluation per iteration
#
#  Update A, B, V, W, and X.
#
        if ( fu <= fx ):

            if ( u < x ):
                sb = x
            else:
                sa = x

            v = w
            fv = fw
            w = x
            fw = fx
            x = u
            fx = fu

        else:

            if ( u < x ):
                sa = u
            else:
                sb = u

            if ( fu <= fw or w == x ):
                v = w
                fv = fw
                w = u
                fw = fu
            elif ( fu <= fv or v == x or v == w ):
                v = u
                fv = fu
        step += 1
        pt.add_row([step, round(sa,7), round(x,7), round(w,7), round(v,7), round(sb,7), \
            round(fx,7), round(fw,7), round(fv,7), round(abs(x-m),7), method])
    return x, fx

def local_min_test ( ):

#*****************************************************************************80
#
## LOCAL_MIN_TEST tests LOCAL_MIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#

    eps = 2.220446049250313E-016

    epsi = np.sqrt ( eps )
    t = 10.0 * np.sqrt ( eps )

    a = 1
    b = 5

    print ( '' )
    print ( 'LOCAL_MIN_TEST' )
    print ( '  Python version: %s' % ( platform.python_version ( ) ) )
    print ( '  LOCAL_MIN seeks a local minimizer of a function F(X)' )
    print ( '' )
    print ( '  g_01(x) = 2 (pi x^2 + 50 / x)' )

    print ( f'  in an interval [A,B] [{a},{b}].' )

    x, fx = local_min ( a, b, epsi, t, g_01 )

    print ( '  g_01(%g) = %g' % ( x, fx ) )

#
#  Terminate.
#
    print(pt)
    print ( '' )
    print ( 'LOCAL_MIN_TEST' )
    print ( '  Normal end of execution.' )
    return

def test_example (f, a, b, t, title ):

#*****************************************************************************80
#
## TEST_EXAMPLE tests LOCAL_MIN on one test function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the endpoints of the interval.
#
#    Input, real T, a positive absolute error tolerance.
#
#    Input, real value = F ( x ), the name of a user-supplied
#    function whose local minimum is being sought.
#
#    Input, string TITLE, a title for the problem.
#
    print ( '' )
    print ( '  %s' % ( title ) )
    print ( '' )
    print ( '  Step      X                          F(X)' )
    print ( '' )

    arg = g_01
    value = f ( arg )
    print ( '  %4d  %24.16e  %24.16e' % ( a, value ) )

    value = f ( arg )
    print ( '  %4d  %24.16e  %24.16e' % ( b, value ) )

    x, fx = local_min ( a2, b2, status, value )

    return


def r8_sign_test ( ):

#*****************************************************************************80
#
## SIGN_TEST tests SIGN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#

    test_num = 5

    r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

    print ( '' )
    print ( 'R8_SIGN_TEST' )
    print ( '  Python version: %s' % ( platform.python_version ( ) ) )
    print ( '  R8_SIGN returns the sign of an R8.' )
    print ( '' )
    print ( '     R8     R8_SIGN(R8)' )
    print ( '' )

    for test in range ( 0, test_num ):
        r8 = r8_test[test]
        s = np.sign ( r8 )
        print ( '  %8.4f  %8.0f' % ( r8, s ) )
#
#  Terminate.
#
    print ( '' )
    print ( 'R8_SIGN_TEST' )
    print ( '  Normal end of execution.' )
    return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#

    t = time.time ( )
    print ( time.ctime ( t ) )

    return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#

    print ( '' )
    print ( 'TIMESTAMP_TEST:' )
    print ( '  Python version: %s' % ( platform.python_version ( ) ) )
    print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
    print ( '' )

    timestamp ( )
#
#  Terminate.
#
    print ( '' )
    print ( 'TIMESTAMP_TEST:' )
    print ( '  Normal end of execution.' )
    return


if ( __name__ == '__main__' ):
    timestamp ( )
    local_min_test ( )
    timestamp ( )
'''
r8_sign_test()

#f = lambda x : 2 * (np.pi * x * x + 50 / x)
a = 1
b = 5
t = 1e-5
title = '  f(x) = 2 (pi x^2 + 50 / x'
test_example (g_01, a, b, t, title )
'''