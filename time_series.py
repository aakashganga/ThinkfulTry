import numpy as np
from datetime import datetime

df = pd.read_csv('LoanStats3b.csv', header=True)

# get column names
list(df.columns.values)

# get # of rows
lendf = len(df)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d'])    


dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year*100+x.month).count()
loan_count_summary = year_month_summary['issue_d'] 

# drop the first row as it is not a datetime
loan_count_summary = loan_count_summary.drop(loan_count_summary.index[0])


# get # of rows
lendf = len(loan_count_summary)


# plot histogram of interest rate
import matplotlib.pyplot as plt
plt.figure()

loan_count_summary.index.set_names(['Date']) # You can assign name to the index

# To plot timeseries, you need to convert the index in the date format of Y-m-d
loan_count_summary.index = pd.to_datetime(loan_count_summary.index, format='%Y%m.0') 


loan_count_summary.plot()

# The time series doesn't look stationary. For a stationary time series, there shouldn't be a trend present i.e. MEAN should be constant over time.


# Since the time series is not stationary, we will need to calculate order of difference
import scikits.statsmodels.tsa.arima_process as tsp
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot


loan_count_summary.plot(figsize=(12,8));

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)

# plot ACF
fig = sm.graphics.tsa.plot_acf(loan_count_summary.values)

# plot PACF
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(loan_count_summary.values)

# Are there any autocorrelated structures in the series? How would you have a model address these structures?
Print "Yes, there are autocorrelated structures as the series tails off"


