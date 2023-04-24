from math import pi
from prettytable import PrettyTable

def opt(a, b, c, fa, fb, fc):
    step = 0
    t = PrettyTable(['step', 'a', 'b', 'c', 'x', 'fa', 'fb', 'fc', 'fx', 'emax'])
    while abs(max(a, c) - min(a, c)) > 1e-6 and step < 19:
        step += 1
        x = b - ((b-a)**2*(fb-fc)-(b-c)**2*(fb-fa))/(2*((b-a)*(fb-fc)-(b-c)*(fb-fa)))
        t.add_row([step, round(a,7), round(b,7), round(c,7), round(x,7), \
        round(fa,7), round(fb,7), round(fc,7), round(f(x),7), round(abs(max([a, b, c]) - min([a, b, c])),7)])
        if fc > fa:
            c = b
            a = a/4+3*x/4
            b = x
            fc = fb
            fa = f(a)
            fb = f(b)
        else:
            a = b
            c = c/4+3*x/4
            b = x
            fa = fb
            fc = f(c)
            fb = f(b)
        print(t)
        return x

def ring(f, lower, upper, stride):
    answers = []
    while lower <= upper:
        seq = lower + stride
        mid = (seq)/2
        answer = opt(lower, mid, seq, f(lower), f(mid), f(seq))
        if answer is not None:
            if answer not in answers:
                answers.append(answer)
        lower += stride
    print(sorted(answers))
    print(str(len(answers))+" solutions!")
    #print(t)

def f(x):
    try:
        y=eval(function)
    except ZeroDivisionError:
        x = 1e-7
    return y


function = "4*pi*r -100/r**2" #"x**3 + x**2 - 3*x - 3" #"2 * (pi*x**2 + 50/x)"
ring(f,0,2,1)