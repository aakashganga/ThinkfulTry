import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

# Convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


# get mean and median of Alcohol column
meanAlcohol=df['Alcohol'].mean()
medianAlcohol=df['Alcohol'].median()

# get mean of Tobacco column
meanTobacco=df['Tobacco'].mean()
medianTobacco=df['Tobacco'].median()

# If all numbers occur equally often, stats.mode() will return the smallest number
modeAlcohol=stats.mode(df['Alcohol'])
modeTobacco=stats.mode(df['Tobacco'])

# Get range, variance and standard deviation
rangeAlchohol = max(df['Alcohol']) - min(df['Alcohol']) # Range of Alcohol
rangeTobacco = max(df['Tobacco']) - min(df['Tobacco']) # Range of Tobacco

stdAlcohol=df['Alcohol'].std() # standard deviation for the Alcohol column
stdTobacco=df['Tobacco'].std() # standard deviation for the Tobacco column

varAlcohol=df['Alcohol'].var() # variance for the Alcohol column
varTobacco=df['Tobacco'].var() # variance for the Tobacco column

print "*********************************************************"
print "The range for Alcohol column is: {}".format(rangeAlchohol)
print "The range for Tobacco column is: {}".format(rangeTobacco)
print "*********************************************************"
print "Mean for Alcohol column is: {}".format(meanAlcohol)
print "Mean for Tobacco column is: {}".format(meanTobacco)
print "*********************************************************"
print "Median for Alcohol column is: {}".format(medianAlcohol)
print "Median for Tobacco column is: {}".format(medianTobacco)
print "*********************************************************"
print "Standard Deviation for Alcohol column is: {}".format(stdAlcohol)
print "Standard Deviation for Tobacco column is: {}".format(meanTobacco)
print "*********************************************************"
print "Mode for Alcohol column is: {}".format(modeAlcohol)
print "Mode for Tobacco column is: {}".format(modeTobacco)
print "*********************************************************"
