import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

# create test data
test_data = np.random.normal(size=1000)   

# Calculate frequencies
c = collections.Counter(test_data)
# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)
  
# draw boxplot
plt.boxplot(test_data)
plt.show()
plt.savefig("boxplot.png")


# draw histogram
plt.hist(test_data, histtype='bar')
plt.show()
plt.savefig("histogram.png")



# draw Q-Q plot for normal distribution
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
plt.savefig("NormQQ.png")


test_data2 = np.random.uniform(size=1000)   

# draw Q-Q plot for uniform distribution
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph
plt.savefig("UniformQQ.png")
