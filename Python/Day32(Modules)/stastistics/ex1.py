import statistics

# Mean = to fIND avg of sample data
# formula = sum of total of num of val /total number of vals

sample = [1,20,35,45,78,98]

#print(statistics.mean([1,20,35,45,78,98]))

#-- To find median of number

# print(statistics.median([1,20,35,45,78,98,45]))

# Mode = most repeated number

# print(statistics.mode([3,4,1,3,2,1,1,2,2]))

# harmonic mean = calcutes the harmonic mean(central location) of the given data
# Formula = (a,b,c,d) --> n/(1/a + 1/b + 1/c + 1/d)

# print(statistics.harmonic_mean([1,2,3,4,5]))

# print(statistics.median_high([2,3,4,87,89,32,21]))

# print(statistics.median_low([2,3,4,5,6,7,8,9]))

# Standard deviation = sqrt( summation(x - mean)**2 / (total number of values - 1))

# print(statistics.pvariance([1,2,3,4,]))
# print(statistics.pstdev([1,2,3,4]))

x = "strukdgfiuavfmkmxsk"

from collections import Counter

y = Counter(x)

print(y)


