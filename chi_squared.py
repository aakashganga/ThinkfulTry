import matplotlib.pyplot as plt
import pandas as pd
import collections
from scipy import stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# drop null values
loansData.dropna(inplace=True)

# get frequency values for open credit lines column
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# calculate the number of instances in the list
count_sum = sum(freq.values())

# to get most frequent number of open credit lines, get mode

# How many unique number of open credit lines are there in the data? : 2498
# What is the most frequent number of open credit lines?

modeloansData=stats.mode(loansData['Open.CREDIT.Lines'])

# The mode is: 8

# draw frequency distribution
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

# Perform a Chi-Squared test (scipy.stats.chisquare)
chi, p = stats.chisquare(freq.values())

print "Chi Squared Value is: {}".format(chi)
print "p-value is: {}".format(p)