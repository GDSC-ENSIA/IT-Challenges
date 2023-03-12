# TODO: 1- import numpy as np
import numpy as np

life_time_sample = [6, 7, 7, 7, 5, 4, 7, 3, 2, 0, 16, 7, 6, 7, 5, 7, 8, 5, 7, 5, 7, 7, 7, 4, 1, 7, 7, 7, 6, 8, 7, 7, 6, 7, 7, 6, 6, 8, 7, 8, 6, 5, 5, 9, 7, 7, 7, 12, 8, 7, 6, 6, 8, 7, 7, 9, 7, 13, 7, 6, 7, 7, 6, 6, 7, 4, 9, 10, 4, 6, 7, 6, 5, 6, 7, 6, 7, 10, 7, 6, 6, 6, 7, 7, 7, 8, 7, 7, 7, 6, 7, 7, 6, 7, 7, 6, 4, 7, 8, 5, 7, 8, 7, 7, 6, 7, 7, 9, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 8, 9]

# TODO: 2- Convert to numpy array
data = np.array(life_time_sample)

# TODO: 3- Calculate mean, rounded to 2 decimal places
mean = np.mean(data).round(2)
print('Mean = ', mean)

# TODO: 4- Calculate median
median = np.median(data)
print('Median = ', median)

# Calculate first quartile Q1
Q1 = np.percentile(data, 25)
print('Q1 = ', Q1)

# TODO: 5- Calculate third quartile Q3
Q3 = np.percentile(data, 75)
print('Q3 = ', Q3)

# TODO: 6- Calculate interquartile range
IQR = Q3 - Q1
print('IQR = ', IQR)

# TODO: 7- Calculate standard deviation, rounded to 2 decimal places
std = np.std(data).round(2)
print('Standard deviation = ', std)

# TODO: 8- Check for outliers
outliers = np.array([x for x in data if (x < Q1 - 1.5 * IQR or x > Q3 + 1.5 * IQR)])
print(outliers)

# Visualize using histogram
import matplotlib.pyplot as plt
plt.hist(data, bins = np.arange(np.min(data), np.max(data) + 1))
plt.show()
