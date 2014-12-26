# Multivariate Linear Regression

import pandas as pd
import collections

loansData = pd.read_csv('C:/Users/amit.dingare/Documents/ScikitLearnTry/Thinkful/LoanStats3a.csv',header=True)

columns_we_want = ['open_acc','int_rate','home_ownership']
loansData_Selected = loansData[columns_we_want]

# Drop null rows
loansData_Selected.dropna(inplace=True)

# to get column names
list(loansData_Selected.columns.values)

# To derive summary statistics of interest rate column
loansData_Selected['int_rate'].describe()

# To derive summary statistics of # of open accounts column
loansData_Selected['open_acc'].describe()

# To derive summary statistics of # of home ownership column
loansData_Selected['home_ownership'].describe()


# get frequencies for 3 volumns used in the model
freq_open_acc = collections.Counter(loansData_Selected['open_acc'])
freq_int_rate = collections.Counter(loansData_Selected['int_rate'])
freq_home_ownership = collections.Counter(loansData_Selected['home_ownership'])

var = loansData_Selected['int_rate'][0:5]  # first 5 rows of Interest.Rate
var = loansData_Selected['open_acc'][0:5]  # first 5 rows of open accounts
loansData_Selected['home_ownership'][0:5] # first 5 rows of home ownership

#cleaning up the columns
# we will use two techniques; map function and lambda
# map() will map the lambda function to each element of what's passed to it. 
#  lambda is an anynomous function that does not need a return statement. It will return the results by default

loansData_Selected['int_rate'] = loansData_Selected['int_rate'].map(lambda x: x.rstrip('%'))

# convert Interest Rate to float
loansData_Selected['int_rate'] = loansData_Selected['int_rate'].astype(float)

# check whether the cleanup has worked
loansData_Selected.head()

# plot histogram of interest rate
import matplotlib.pyplot as plt
plt.figure()
loansData_Selected['int_rate'].hist() # to draw a histogram, first convert FICO.Range column to interger and then use hist function
plt.show()

# plot histogram of interest rate
import matplotlib.pyplot as plt
plt.figure()
loansData_Selected['open_acc'].hist() # to draw a histogram, first convert FICO.Range column to interger and then use hist function
plt.show()


# now we are going to build linear regression
from statsmodels.formula.api import ols
import numpy as np

model = ols('int_rate ~ open_acc', loansData_Selected)
f = model.fit()

# to get summary of the model
f.summary()
# And output the results:

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[0]
print 'P-Values are: ', f.pvalues
print 'R-Squared: ', f.rsquared

# The model looks as follows: 
# int_rate = 11.9762+0.02*openacc
# The model has an R-Squared:  0.000611809545496 and coefficients are statistically significant

# now add home ownership to the model

assert isinstance(loansData_Selected, object)
model2 = ols('int_rate ~ open_acc + C(home_ownership) ', loansData_Selected)
f2 = model2.fit()


# to get summary of the model
f2.summary()
# And output the results:

print 'Coefficients: ', f2.params[0:5]
print 'Intercept: ', f2.params[0]
print 'P-Values: ', f2.pvalues
print 'R-Squared: ', f2.rsquared

# Does that affect the significance of the coefficients in the original model?
# Yes, Open Account became more significant

# Try to add the interaction of home ownership and incomes as a term. How does this impact the new model?
model3 = ols('int_rate ~ open_acc * C(home_ownership) ', loansData_Selected)
f3 = model3.fit()

# to get summary of the model
f3.summary()
# And output the results:

print 'Coefficients: ', f3.params[0:5]
print 'Intercept: ', f3.params[0]
print 'P-Values: ', f3.pvalues
print 'R-Squared: ', f3.rsquared
