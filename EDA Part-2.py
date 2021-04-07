#EDA Part-2
#Visualizations
import matplotlib.pyplot as plt
#pandas library provides read_csv() for importing a csv dataset
import pandas as pd
d=pd.read_csv("E:\Chrome downloads\Salary_Data.csv")

#1.Histogram
#Histogram of YearsExperience in Salary_Data
plt.hist(d["YearsExperience"])
#Histogram of Salary in Salary_Data
plt.hist(d["Salary"])

#2.Barplot
#Barplot of YearsExperience vs Salary
plt.bar(d["YearsExperience"],d["Salary"])

#3.Boxplot
#Boxplot of YearsExperience
plt.boxplot(d["YearsExperience"])
#Boxplot of Salary
plt.boxplot(d["Salary"])

