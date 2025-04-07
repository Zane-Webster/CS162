import matplotlib.pyplot as plot

# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['green', 'pink', 'yellow', 'red']
explodelist = [0.05, 0.05, 0.05, 0.05]

# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 180)

plot.axis('equal')
plot.savefig('bin/piechart.png')
