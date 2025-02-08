import numpy
from matplotlib import pyplot

mydata = numpy.loadtxt("daily_steps.csv", delimiter=",", dtype=str)

days = [item.strip() for item in mydata[0]]
steps = numpy.array(mydata[1], dtype=int)
pyplot.bar(days, steps)