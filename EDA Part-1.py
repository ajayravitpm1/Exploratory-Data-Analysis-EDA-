#EDA Part-1
#First,second,third and fourth moment business decisions

#pandas library provides read_csv() for importing a csv dataset
import pandas as pd
#numpy library provides mean() and median() functions to calculate mean and median
import numpy as np
#statistics library provides stdev() function to calculate standard deviation and variance() function to calculate variance
import statistics
#importing dataset
d=pd.read_csv("E:\Chrome downloads\Salary_Data.csv")
#1.First moment business decision-Measures of central tendency
print(round(np.mean(d["YearsExperience"]),2)) #a)mean
print(round(np.median(d["YearsExperience"]),2)) #b)median
print((statistics.mode(d["YearsExperience"]))) #c)mode
#2.Second moment business decision-Measures of dispersion
print(round(statistics.variance(d["YearsExperience"]),2)) #a)variance
print(round(statistics.stdev(d["YearsExperience"]),2)) #b)standard deviation
print(max(d["YearsExperience"])-min(d["YearsExperience"])) #c)range
#3.Third moment business decision
print(d.skew(axis=0,skipna=True)) #skewness
#4.Fourth moment business decision
print(d.kurtosis(axis=0,skipna=True)) #kurtosis
