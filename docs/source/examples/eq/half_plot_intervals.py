import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()
pt1 = [1.75,0.172]
pt2 = [1.625,-0.943]
pt3 = [1.6875,-0.409]
pt4 = [1.719,-0.125]
pt5 = [1.734,0.022]
pt6 = [1.726,-0.052]
pt7 = [1.73,-0.015]
pt8 = [1.732,0.0035]
pt9 = [1.731,-0.005]
pt10 = [1.732,-0.001]
pt11 = [1.732,-0.001]
pt12 = [1.732,-0.001]

#x_vals= [pt1[0],pt2[0],pt3[0],pt4[0],pt5[0],pt6[0],pt7[0],pt8[0],pt9[0]
        #,pt10[0],pt11[0],pt12[0]]
#y_vals= [pt1[1],pt2[1],pt3[1],pt4[1],pt5[1],pt6[1],pt7[1],pt8[1],pt9[1]
        #,pt11[1],pt11[1],pt12[1]]

x = np.linspace(1, 2.5)
#plt.figure(figsize=(12,6))
plt.plot(x, x**3 + x**2 -3*x -3)
plt.plot([0,3], [0,0], 'g')

'''
plt.plot([pt1[0],pt2[0]], [pt1[1],pt2[1]], 'ko-')
plt.plot([pt3[0],pt4[0]], [pt3[1],pt4[1]], 'ko-')
plt.plot([pt5[0],pt6[0]], [pt5[1],pt6[1]], 'ko-')
plt.plot([pt7[0],pt8[0]], [pt7[1],pt8[1]], 'ko-')
plt.plot([pt9[0],pt10[0]], [pt9[1],pt10[1]], 'ko-')
'''
plt.vlines(pt1[0], 0, pt1[1], 'c', label='1st interpolation')
plt.vlines(pt2[0], 0, pt2[1], 'm', label='2nd interpolation')
plt.vlines(pt3[0], 0, pt3[1], 'y', label='3rd interpolation')
plt.vlines(pt4[0], 0, pt4[1], 'brown', label='4th interpolation')
plt.vlines(pt5[0], 0, pt5[1], 'r', label='5th interpolation')

plt.scatter(pt1[0], pt1[1], fc='none', ec='c')
plt.scatter(pt2[0], pt2[1], fc='none', ec='m')
plt.scatter(pt3[0], pt3[1], fc='none', ec='y')
plt.scatter(pt4[0], pt4[1], fc='none', ec='brown')
plt.scatter(pt5[0], pt5[1], fc='none', ec='r')


plt.scatter(pt1[0], 0, fc='none', ec='c')
plt.scatter(pt2[0], 0, fc='none', ec='m')
plt.scatter(pt3[0], 0, fc='none', ec='y')
plt.scatter(pt4[0], 0, fc='none', ec='brown')
plt.scatter(pt5[0], 0, fc='none', ec='r')

plt.text(pt1[0]+0.003, 0.012, "x1")
plt.text(pt2[0]+0.003, 0.012, "x2")
plt.text(pt3[0]+0.003, 0.012, "x3")
plt.text(pt4[0]-0.009, 0.018, "x4")
plt.text(pt5[0]+0.001, -0.1, "x5")

plt.text(pt1[0]+0.006, pt1[1]-0.006, "y1")
plt.text(pt2[0]+0.006, pt2[1]-0.008, "y2")
plt.text(pt3[0]+0.006, pt3[1]-0.010, "y3")
plt.text(pt4[0]+0.006, pt4[1]-0.010, "y4")
plt.text(pt5[0]-0.012, pt5[1], "y5")

plt.grid(True)
plt.ylim((-1.5,0.5))
plt.xlim((1.6,1.8))
plt.title('Half Interval Solution')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend()
plt.show()
#plt.savefig('../../figures/half_intervals.png')
