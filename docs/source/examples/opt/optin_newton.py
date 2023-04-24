import math
from prettytable import PrettyTable

def deriv(df, x):
    h = 1e-8
    return (df(x+h) - df(x))/h

def opt(df, x0):
    xn = x0
    step = 0
    err = 1e-6
    max_iter = 19
    y = df(xn)
    for n in range(0,max_iter):
        y=df(xn)
        if abs(y)<err:
            return xn
        slope=deriv(df,xn)
        if(slope==0):
            return None
        xn=xn-y/slope
    return None
    '''
    while step < max_iter and y > err:
        slope = deriv(df, xn)
        if slope == 0:
            return None
        xn = xn - y/slope
        step += 1
        return xn
    '''
def ring(df, lower, upper, stride):
    answers = []
    while lower <= upper:
        seq = lower + stride
        mid = (seq)/2
        answer = opt(df, lower)
        print(answer)
        if answer is not None:
            if answer not in answers:
                answers.append(answer)
        lower += stride
    print(sorted(answers))
    print(str(len(answers))+" solutions!")

def df(x):
    try:
        y=eval(equation)
    except ZeroDivisionError:
        y= 1e-10
    return y

equation="math.sin(x) - x/2"

ring(df, -10, 10, 1)