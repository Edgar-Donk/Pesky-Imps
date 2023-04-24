import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

f = lambda x: 2 * (np.pi*x**2 + 50/x)

def alpha(a,b,fa,fb):
    return (fb-fa)/(b-a)

def beta(alpha,a,b,c,fa,fb,fc):
    return (fc-fa-alpha(a,b,fa,fb)*(c-a))/((c-a)*(c-b))

x = [1, 3, 5]
y = fa, fb, fc = f(x[0]),f(x[1]),f(x[2])


xx = np.linspace(min(x), max(x))

xp = (x[0]+x[1])/2 - alpha(x[0],x[1],fa,fb)/(2*beta(alpha,*x,*y))
yp = fa + alpha(x[0],x[1],fa,fb)*(xp - x[0]) + beta(alpha,*x,*y) * \
        (xp - x[0]) * (xp - x[1])

x2 = [(x[0]/4+3*xp/4), xp, 3]
y2 = fa2, fb2, fc2 = f(x2[0]),f(x2[1]),f(x2[2])
xx2 = np.linspace(min(x2), max(x2))

xp2 = (x2[0]+x2[1])/2 - alpha(x2[0],x2[1],fa2,fb2)/(2*beta(alpha,*x2,*y2))
yp2 = fa2 + alpha(x2[0],x2[1],fa2,fb2)*(xp2 - x2[0]) + beta(alpha,*x2, \
        *y2) * (xp2 - x2[0]) * (xp2 - x2[1])

x3 = [(x2[0]/4+3*xp2/4), xp2, xp]
y3 = fa3, fb3, fc3 = f(x3[0]),f(x3[1]),f(x3[2])
xx3 = np.linspace(min(x3), max(x3))

xp3 = (x3[0]+x3[1])/2 - alpha(x3[0],x3[1],fa3,fb3)/(2*beta(alpha,*x3,*y3))
yp3 = fa3 + alpha(x3[0],x3[1],fa3,fb3)*(xp3 - x3[0]) + beta(alpha,*x3, \
        *y3) * (xp3 - x3[0]) * (xp3 - x3[1])

x4 = [(x3[0]/4+3*xp3/4), xp3, xp2]
y4 = fa4, fb4, fc4 = f(x4[0]),f(x4[1]),f(x4[2])
xx4 = np.linspace(min(x4), max(x4))

xp4 = (x4[0]+x4[1])/2 - alpha(x4[0],x4[1],fa4,fb4)/(2*beta(alpha,*x4,*y4))
yp4 = fa4 + alpha(x4[0],x4[1],fa4,fb4)*(xp4 - x4[0]) + beta(alpha,*x4, \
        *y4) * (xp4 - x4[0]) * (xp4 - x4[1])

x5 = [(x4[0]/4+3*xp4/4), xp4, xp3]
y5 = fa5, fb5, fc5 = f(x5[0]),f(x5[1]),f(x5[2])
xx5 = np.linspace(min(x5), max(x5))

xp5 = (x5[0]+x5[1])/2 - alpha(x5[0],x5[1],fa5,fb5)/(2*beta(alpha,*x5,*y5))
yp5 = fa5 + alpha(x5[0],x5[1],fa5,fb5)*(xp5 - x5[0]) + beta(alpha,*x5, \
        *y5) * (xp5 - x5[0]) * (xp5 - x5[1])

plt.plot(xx, f(xx), 'b', label='function')

plt.plot(xx, fa+alpha(x[0],x[1], \
    fa,fb)*(xx-x[0])+beta(alpha,*x,*y)*(xx-x[0])* \
    (xx-x[1]), 'g', label='1st quadratic')
plt.plot(xx2, fa2+alpha(x2[0],x2[1], \
    fa2,fb2)*(xx2-x2[0])+beta(alpha,*x2,*y2)*(xx2-x2[0])* \
    (xx2-x2[1]), 'y', label='2nd quadratic')
plt.plot(xx3, fa3+alpha(x3[0],x3[1], \
    fa3,fb3)*(xx3-x3[0])+beta(alpha,*x3,*y3)*(xx3-x3[0])* \
    (xx3-x3[1]), 'm', label='3rd quadratic')
plt.plot(xx4, fa4+alpha(x4[0],x4[1], \
    fa4,fb4)*(xx4-x4[0])+beta(alpha,*x4,*y4)*(xx4-x4[0])* \
    (xx4-x4[1]), 'r', label='4th quadratic')
plt.plot(xx5, fa+alpha(x5[0],x5[1], \
    fa5,fb5)*(xx5-x5[0])+beta(alpha,*x5,*y5)*(xx5-x5[0])*(xx5-x5[1]), \
     'c', label='5th quadratic')

plt.scatter(x, y, fc='none', ec='k', label='starting points',s=80)

plt.scatter(x2, y2, fc='none', ec='y', label='2nd set points',s=80)
plt.scatter(x3, y3, fc='none', ec='m', label='3rd set points',s=80)
plt.scatter(x4, y4, fc='none', ec='r', label='4th set points',s=80)
plt.scatter(x5, y5, fc='none', ec='c', label='5th set points',s=80)

plt.plot(xp, yp, 'gP', label='1st quadratic minimum')
plt.plot(xp2, yp2, 'yP', label='2nd quadratic minimum')
plt.plot(xp3, yp3, 'mP', label='3rd quadratic minimum')
plt.plot(xp4, yp4, 'rP', label='4th quadratic minimum')
plt.plot(xp5, yp5, 'cP', label='5th quadratic minimum')
plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('More Aggressive Adjusting Limits\nSuccessive Quadratic Interpolation')
plt.show()
#plt.savefig('../../figures/succ_para2.png')

