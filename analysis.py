# import packages
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create a data series
# series work kind of like lists
# use for one-dimensional data
mySeries = Series([4, 3, 5, np.nan, 6, 8])
print mySeries
mySeries.values
mySeries.index

mySeries2 = Series([3,5,7,9], index=['d', 'c', 'a', 'b'])
print mySeries2
# check the values
mySeries2.values
mySeries2.index

mySeries[1]
mySeries2['d']
mySeries[['c', 'a', 'd']]
mySeries2[mySeries2 > 0] # equivalent to which() in R
myDoubled = mySeries * 2 # perform functions on your arrays
np.exp(myDoubled)

# check whether values appear in an index
'b' in mySeries2
'e' in mySeries2

# examining the data
mySeries.head()
mySeries.tail()
mySeries.shape
mySeries.mean()
mySeries.median()
mySeries.std()
mySeries.sum()
mySeries.describe()

# how would you compute these summary stats without the built-in functions?



# DataFrames are useful for multidimentional data
# let's load data from a remote file
data = pd.read_csv("https://github.com/mcdickenson/2016-05-19-general-assembly/raw/master/data.csv")

# take a look at the data
data.head()
data.tail()
data.shape
data.mean()
data.median()
data.std()
data.sum()
data.describe()

# retrieve specific column
data[[0]]
data['country']

# retrieve specific rows
data[1:4]

# rows and columns
data[1:4][[0]]
# order of indices doesn't matter!
data[[0]][1:4]
# why is this?

# we can access the data in more interesting ways too
data[data['country'] == 'Spain']
# this can include multiple values
data[data['roundabouts'] > 15]

# what was the minimum number of fatalities?
data['fatalities'].min()
# in which country was that?
data[data['fatalities'] == data['fatalities'].min()]['country']
# again, order doesn't matter
data['country'][data['fatalities'] == data['fatalities'].min()]


# # we can also apply functions to columns
fmt = lambda x: '%.2f' % x
data['roundabouts'].map(fmt)

# sort on values
data2 = data.sort_index(by='fatalities')
print data2

# what's the maximum number of roundabouts?
# in which country is that?


# we can create new columns
data['fatalities_per_roundabout'] = data['fatalities'] / data['roundabouts']
print data

# we can also delete them
del data['fatalities_per_roundabout']
print data



# Visualizing data
fig = plt.figure()
plot.scatter(data['roundabouts'], data['fatalities'])
fig.savefig("graph1.png")

# let's calculate the correlation
data['roundabouts'].corr(data['fatalities'])

# now let's fit a linear regression
model = pd.ols(y=data['fatalities'], x=data['roundabouts'])
print model
# have a look at the coefficients
model.beta

# predict fatalities based on the model
data['yhat'] = model.beta['intercept'] + model.beta['x'] * data['roundabouts']

# plot line of best fit
fig = plt.figure()
plt.scatter(data['roundabouts'], data['fatalities'])
plt.plot(data['roundabouts'], data['yhat'], 'r')
fig.savefig("graph2.png")

# now let's make the plot a bit more readable
fig = plt.figure()
plt.xlabel('Roundabouts per 1,000 intersections')
plt.ylabel('Traffic fatalities per 100,000 inhabitants')
plt.title('Roundabouts and Safety')
plt.scatter(data['roundabouts'], data['fatalities'])
plt.plot(data['roundabouts'], data['yhat'], 'r')
plt.show()
fig.savefig("graph3.png")

# which country's predicted value is closest to its actual value?
# which country's predicted value is furthest from its actual value?
# (hint: creating an extra column might help answer this)

