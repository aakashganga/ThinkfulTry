# -*- coding: utf-8 -*-
# Logistics Regression

import pandas as pd
import collections
loansData.to_csv('loansData_clean.csv', header=True, index=False)

# Add a column to your dataframe indicating whether the interest rate is < 12%.
loansData['Low.Int.Flag'] = loansData['Interest.Rate'] < 12

# Do some spot checks to make sure that it worked.
loansData[loansData['Interest.Rate'] <= 10].head() # should all be True
loansData[loansData['Interest.Rate'] >= 13].head() # should all be False

# now we are going to build linear regression
import statsmodels.api as sm
import numpy as np

# We'll use the cleaned loansData DataFrame we've been using and extract some columns:

intflag = loansData['Low.Int.Flag']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']

# When we extract a column from a DataFrame, it's returned as a Series datatype. You want to reshape the data like this:

# The dependent variable
y = np.matrix(intflag).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Now you want to put the two columns together to create an input matrix (with one column for each independent variable):
x = np.column_stack([x1,x2])

# Now we create a linear model:

ind_vars = sm.add_constant(x) # this add a constant intercept of 1.0

# build the model
logit = sm.Logit(y, ind_vars)
result = logit.fit()

# Summary of resu;ts
# And output the results:

print 'Coefficients: ', result.params[0:2]
print 'Intercept: ', result.params[0]
print 'P-Values: ', result.pvalues

# The logistic model is
# interest_rate = −60.125 + 0.087423(FicoScore) − 0.000174(LoanAmount)

# What is our logistic function?
# p(x) = 1/(1 + e^(−60.125 + 0.087423(FicoScore) − 0.000174(LoanAmount))

def logistic_function(FicoScore, LoanAmount):
    interest_rate = result.params[0] + result.params[1]*FicoScore+result.params[2]*LoanAmount
    prob_interest_rate  = 1/(1+e**interest_rate)
    return prob_interest_rate

# Determine the probability that we can obtain a loan at ≤12% Interest for $10,000 with a FICO score of 720 using this function.
logistic_function(720,10000)

# Ans is 0.2540

# Is p above or below 0.70? Do you predict that we will or won't obtain the loan?

# since p is below 0.7, we won't obtain the loan


    


