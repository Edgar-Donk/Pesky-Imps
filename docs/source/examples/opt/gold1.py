import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from numpy import linspace, sqrt
import seaborn as sns

sns.set_theme()

fig = plt.figure() # figsize=(7,1)

phi_inv = 2 /(sqrt(5) + 1)  # inverse phi, when used always in multiplication

x = linspace(-2, 6)
y = (x-2)**2 + 6

f = lambda x: (x-2)**2 + 6 # 2 * (pi*r**3 + 50/r)


# points
xl = -1
xu = 6

x1 = xu - (xu - xl) * phi_inv
x2 = xl + (xu - xl) * phi_inv

xs = [xl, x1, x2, xu]
Fl = f(xl)
F1 = f(x1)
F2 = f(x2)
Fu = f(xu)
ys = [Fl, F1, F2, Fu]
y0 = [0, 0, 0, 0]

x1n = x2-(x2-xl)*phi_inv
xln, x2n, xun = xl, x1, x2
xns = [xln, x1n, x2n, xun]
Fln, F1n, F2n, Fun = Fl, f(x1n), F1, F2
yns = [Fln, F1n, F2n, Fun]
yn0 = [0, 0, 0, 0]

plt.plot(x,y, lw=2, color='k', label='function')
plt.plot(xs, ys, 'mo', label='initial points')
plt.plot(xs, y0, 'mo')
plt.plot(xns, yns, 'bo', label='1st iteration')
plt.plot(xns, yn0, 'bo')

plt.vlines(x=x1+0.03, ymin=0, ymax=F1, colors='m', ls='--')
plt.vlines(x=x2, ymin=0, ymax=F2, colors='m', ls='--')
plt.vlines(x=x1n, ymin=0, ymax=F1n, colors='b', ls='--')
plt.vlines(x=x2n-0.03, ymin=0, ymax=F2n, colors='b', ls='--')

plt.annotate('f(xl)', xy = (xl+0.3, f(xl)+0.3), color='m')
plt.annotate('f(x1)', xy = (x1, f(x1)+0.4), color='m')
plt.annotate('f(x2)', xy = (x2+0.2, f(x2)), color='m')
plt.annotate('f(xu)', xy = (xu, f(xu)+0.3), color='m')

plt.annotate('xl', xy = (xl+0.1, 0.4), color='m')
plt.annotate('x1', xy = (x1+0.1, 0.4), color='m')
plt.annotate('x2', xy = (x2+0.1, 0.4), color='m')
plt.annotate('xu', xy = (xu, 0.4), color='m')

plt.annotate('xln', xy = (xln+0.1, -0.3), color='b')
plt.annotate('x1n', xy = (x1n+0.1, -0.3), color='b')
plt.annotate('x2n', xy = (x2n+0.1, -0.3), color='b')
plt.annotate('xun', xy = (xun+0.1, -0.3), color='b')

plt.annotate('f(xln)', xy = (xln+0.3, Fln-0.6), color='b')
plt.annotate('f(x1n)', xy = (x1n+0.2, F1n-0.4), color='b')
plt.annotate('f(x2n)', xy = (x2n+0.1, F2n-0.9), color='b')
plt.annotate('f(xun)', xy = (xun+0.2, Fun-0.9), color='b')

plt.annotate(text='', xy=(x2,-1), xytext=(xl,-1), arrowprops=dict(arrowstyle='<->', color='m'))
plt.annotate(text='', xy=(xu,-1.5), xytext=(x1,-1.5), arrowprops=dict(arrowstyle='<->', color='m'))
plt.annotate(text='', xy=(x2n,-2.0), xytext=(xln,-2.0), arrowprops=dict(arrowstyle='<->', color='b'))
plt.annotate(text='', xy=(xun,-2.5), xytext=(x1n,-2.5), arrowprops=dict(arrowstyle='<->', color='b'))

plt.ylim(-4,20)
plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Optimisation by Golden Ratio \n on function $(x-2)^2 + 6$')
#plt.show()
plt.savefig('../../figures/max_gold.png')