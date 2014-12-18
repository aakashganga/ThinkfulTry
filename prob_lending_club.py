import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#To start off with, we need to remove rows with null values so that we can better visualize the dataset.
loansData.dropna(inplace=True)

# EDA
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()
plt.savefig("Investpr_boxplot.png")

# It appears that the median is $10,000 and 75% of the loans are between $6,000 and $16,000

# Generate histogram of loan amounts
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()
plt.savefig("Investpr_histogram.png")

# The historgram shows the frequency distribution at various loan amounts

# Check normality of the data by generating Q-Q plots
import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()
plt.savefig("Investpr_QQ.png")

# The Q-Q plot shows that the data is not distributed normally.