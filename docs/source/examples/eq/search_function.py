# https://medium.com/swlh/finding-a-functions-roots-with-python-590eca0d22a5
import math
def derivative(f, x):
    h=1e-8
    return (f(x+h)-f(x))/h
def solver(f, x0, epsilon, max_iter):
    xn=x0
    for n in range(0,max_iter):
        y=f(xn)
        if abs(y)<epsilon:
            return xn
        slope=derivative(f,xn)
        if(slope==0):
            return None
        xn=xn-y/slope
    return None
def loop(f, L_bound, R_bound, increment):
    solutions=[]
    while L_bound<=R_bound:
        solution=solver(f, L_bound, 1e-10, 1000)
        if solution is not None:
            solution=round(solution,4)
            if solution not in solutions:
                solutions.append(solution)
        L_bound+=increment
    print(sorted(solutions))
    print("we found "+str(len(solutions))+" solutions!")
    equation=""
def f(x):
    try:
        y=eval(equation)
    except ZeroDivisionError:
        y= 1e-10
    return y
equation="math.sin(x) - x/2"
loop(f,-10,10,10)
#[-1.8955, 0.0, 1.8955]
#we found 3 solutions!