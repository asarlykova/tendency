# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
# =============================================================================
# This is part for  practice from W3shcool codes
# =============================================================================
print('This code will print mean, std, percentile, minimum and maxium \n',df.describe())

percentile=df['Maxpulse']
result=np.percentile(percentile,20)
print('Prints 20th percentile:  \n',result)

std = np.std(df)
print('Calculating standard deviation:  \n',std)

cv = np.std(df) / np.mean(df)
print('Get an idea of how large the standard deviation:  \n',cv)

var = np.var(df)
print('To find the variance:  \n',var)


print('Show relation btw 2 variables in line')
df.plot(x ='Pulse', y='Duration', kind='scatter')
plt.show()

print('This will print coorelation matrix')
Corr_Matrix = round(df.corr(),2)
print(Corr_Matrix)





# =============================================================================
# Explain the major central and variance of data 
#(like Percentiles, Standard Deviation, Variance, Correlation, Correlation Matrix,
# Correlation vs Causality) with python code and submit the python practice file.")
# =============================================================================
import pandas as pd
pd.options.display.max_rows=50
file = pd.read_csv('fifa_players.csv') 
print(file.describe())
print(file)
# =============================================================================
# The data is so large that is why we are taking only 50 rows and 7 coumns
# in other words only top 50 fifa players adh their name, age, height, weight 
# =============================================================================
print('Percentile - will print out the number wich is greater than the given percent')
age=file['age']
p25=np.percentile(age, 25)
print('25% of players younger than :', p25)
p50=np.percentile(age, 50)
print('50% of players younger than :', p50)
p75=np.percentile(age, 75)
print('75% of players younger than :', p75)
# =============================================================================
# Here we should use column name, because Rercentile works for only numbers 
# =============================================================================
print('Standard deviation - a number that describes how spread out the observations are')
stan = np.std(file['age'])
print('Spread out:',stan)
# =============================================================================
# A low standard deviation means that most of the numbers are close to the mean value.
#A high standard deviation means that the values are spread out over a wider range.
# =============================================================================
print('Coefficient of Variation - used to get an idea of how large the standard deviation is')
cv = np.std(file['weight_kgs']) / np.mean(file['weight_kgs'])
print('Standard deviation:',cv)
# =============================================================================
# Here our number is small, it means that players weights are almost closed 
# =============================================================================
print('Variance - is another number that indicates how spread out the values are')
spr = np.var(file['height_cm'])
print('Variance:',spr)
# =============================================================================
# If you take the square root of the variance, you get the standard deviation
# =============================================================================

print('Correlation measures the relationship between two variables')
file.plot(x ='height_cm', y='weight_kgs', kind='scatter')
plt.show()

file.plot(kind='hist')
plt.show()

file.plot()
plt.show()
# =============================================================================
# Here players height and weight are compeared and plots diogram by given kind 
# =============================================================================
numeric_columns = ['age', 'height_cm', 'weight_kgs', 'overall_rating','potential', 'value_euro', 'wage_euro']
data = pd.read_csv('fifa_players.csv', usecols=numeric_columns)
data.plot()
plt.show()
# =============================================================================
# 
# =============================================================================
correlation_matrix = data.corr()
print("Correlation Matrix:")
print(correlation_matrix)
# =============================================================================
# This will print out correlation in matrix 
# =============================================================================
import seaborn as sns
axis_corr = sns.heatmap(correlation_matrix,vmin=-1, vmax=1, center=0,cmap=sns.diverging_palette(50, 500, n=500),square=True)
plt.show()
# =============================================================================
# Here we use the Seaborn library to create a correlation heat map 
# =============================================================================
