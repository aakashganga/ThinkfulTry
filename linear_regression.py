# Linear Regression

import pandas as pd
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Drop null rows
loansData.dropna(inplace=True)

# To derive summary statistics
loansData['Interest.Rate'].describe()


freq = collections.Counter(loansData['Open.CREDIT.Lines'])

loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate
loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length
loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range


#cleaning up the columns
# we will use two techniques; map function and lambda
# map() will map the lambda function to each element of what's passed to it. 
#  lambda is an anynomous function that does not need a return statement. It will return the results by default

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

# Next, we need to convert get the lowest of the FICO score


temp = loansData['FICO.Range'].map(lambda x: x.split('-')) # this splits the range into two values
loansData['FICO.Range'] =  tuple(x[0] for x in temp) # this goes through the values and gets the first value

# convert Fico Range, Interest Rate and Loan Length to integers

loansData['FICO.Range'] = loansData['FICO.Range'].astype(int)
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
loansData['Loan.Length'] =  loansData['Loan.Length'].astype(int)

# check whether the cleanup has worked
loansData.head()

# plot histogram of FICO Score
import matplotlib.pyplot as plt
plt.figure()
loansData['FICO.Range'].hist() # to draw a histogram, first convert FICO.Range column to interger and then use hist function
plt.show()


# Generate a Scatter-plot of the Data
# A scatterplot matrix is a grid of plots of multiple variables that shows the relationship of each variable to each of the others.
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

# There is an approximate but unmistakeable linear trend between FICO Score and Interest Rate, 
# while there is no apparent trend between Monthly Income and Interest Rate. 
# Similarly there is no obvious variation in the Monthly Income plot for Loan Length, 
# but there is a distinct and increasing trend in the Monthly Income plot for Loan Amount.

# So what does this suggest? It suggests that we should use FICO Score and Loan Amount in our model as independent variables, 
# while Monthly Income and Loan Length don't seem to be too useful as independent variables.

# now we are going to build linear regression
import statsmodels.api as sm
import numpy as np

# We'll use the cleaned loansData DataFrame we've been using and extract some columns:

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']

# When we extract a column from a DataFrame, it's returned as a Series datatype. You want to reshape the data like this:

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Now you want to put the two columns together to create an input matrix (with one column for each independent variable):
x = np.column_stack([x1,x2])

# Now we create a linear model:

X = sm.add_constant(x) # this add
model = sm.OLS(y,X)
f = model.fit()

# And output the results:

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared