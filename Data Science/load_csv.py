import numpy

# load the csv file by treating data in it as string
# data = numpy.loadtxt("example.csv", delimiter= ",", dtype=str)
# print(data)

# read the csv file and load into a dict
# skip first row
walk_data = numpy.loadtxt("walk_steps.csv", delimiter=",", skiprows=1, dtype=str)

walk_dict = dict()

for mylist in walk_data:
    walker = mylist[0]
    walk_dict[walker] = numpy.array(mylist[1:], dtype=int)

print(walk_dict)