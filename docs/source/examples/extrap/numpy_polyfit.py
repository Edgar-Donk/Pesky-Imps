import numpy, matplotlib
import matplotlib.pyplot as plt

xData = numpy.array([1.1, 2.2, 3.3, 4.4, 5.0, 6.6, 7.7, 0.0])
yData = numpy.array([1.1, 20.2, 30.3, 40.4, 50.0, 60.6, 70.7, 0.1])

polynomialOrder = 2 # example quadratic

# curve fit the test data
fittedParameters = numpy.polyfit(xData, yData, polynomialOrder)
#fittedParameters = numpy.polynomial.polynomial.Polynomial.fit(xData, yData, polynomialOrder, window=[0, 10])
print('Fitted Parameters:', fittedParameters)

modelPredictions = numpy.polyval(fittedParameters, xData)
absError = modelPredictions - yData

SE = numpy.square(absError) # squared errors
MSE = numpy.mean(SE) # mean squared errors
RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (numpy.var(absError) / numpy.var(yData))
print('RMSE:', RMSE)
print('R-squared:', Rsquared)

print()


##########################################################
# graphics output section
def ModelAndScatterPlot(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot
    axes.plot(xData, yData,  'D')

    # create data for the fitted equation plot
    xModel = numpy.linspace(min(xData), max(xData))
    yModel = numpy.polyval(fittedParameters, xModel)

    # now the model as a line plot
    axes.plot(xModel, yModel)

    axes.set_xlabel('X Data') # X axis data label
    axes.set_ylabel('Y Data') # Y axis data label

    plt.show()
    plt.close('all') # clean up after using pyplot

graphWidth = 800
graphHeight = 600
ModelAndScatterPlot(graphWidth, graphHeight)