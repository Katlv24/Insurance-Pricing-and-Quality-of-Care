# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 06:15:36 2020

@author: kathe
"""
import pandas as pd
from pandas import plotting
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy
from scipy import stats
import os
#%% 
file = r'C:\Users\kathe\Downloads\Healthcaredata.csv'
os.path.exists(file)
#locating the file
#%%
dataset=pd.read_csv(r'C:\Users\kathe\Downloads\Healthcaredata.csv')
df=pd.DataFrame(dataset) 
print(dataset)
print(dataset.describe())
print(list(df))
varnames = list(df)
#States, Rank, Score, Cost
#%%
Average = 117, 53
#when the descbring the data, the averages pulled for the Score for the 51 outputs, however, the cost never produced a mean.
#The average 117, was done by caculator for the Cost
Names = ("Cost", "Score")
plt.bar(Names, Average, label="Section1")
plt.ylabel("Score")
plt.xlabel("Cost")
plt.title("Healthcare in the US")
plt.show()
#Histogram
labels=['Score','Cost']
exp_data=[53,117]
p=plt.pie(exp_data,labels=labels)
plt.title('Healthcare in the US')
plt.show()
#Pie Chart
#Very similar, yet obvious results. 
#But this is just the easy view, how heteroscedatic is this data?
#%%
dataset1 = [188, 92, 85, 187, 83, 144, 99, 114, 99, 97, 84, 74, 102, 85, 88, 109, 94, 131, 93, 79, 388, 87, 73, 105, 81, 86, 111, 381, 372, 145, 171, 85, 96, 80, 91, 104, 104, 0, 89, 89, 70, 125, 64, 0, 101, 117, 289, 0, 119, 99, 67]
print(dataset1)
dataset2 = [43.83, 46.83, 47.4, 45.61, 50.52, 59.06, 57.69, 55.26, 60.72, 49.01, 43.76, 58.59, 50.99, 54.27, 51.7, 58.7, 57.14, 52.62, 43.82, 57.37, 56.78, 63.47, 55.24, 63.11, 44.36, 50.2, 57.59, 53.73, 48.38, 57.41, 55.04, 51.84, 52.58, 44.32, 60.7, 54.35, 47.92, 51.32, 56.61, 62.22, 46.57, 57.81, 46.55, 46.8, 55.72, 59.49, 55.53, 49.93, 48.18, 56.42, 51.66 ]
print(dataset2)
x = dataset2
y = dataset1
plt.scatter(x, y)
plt.title('Scatter plot of Score vs Cost log')
plt.xlabel('Score')
plt.ylabel('Cost')
plt.show()
#%%
sns.regplot(x= dataset2, y= dataset1,  color = 'pink', data=df )
#Line of best fit shows that while the scatter plot seems to similar bunches, many points are stdeviations away
#%%
#Taking the prices of these states by rankings 1, 2, 3, 4, 47 48, 49, 50
#Ho: There is correlation, if crit-value in parameters
Sample= np.array([87, 105, 89, 114, 81, 96, 97, 84])
x = scipy.stats.ttest_1samp(Sample, 8)
print(x)
mu= np.mean(Sample)
sd = np.std(Sample)
print(mu)
print(sd)
sqn=2.82
print(sqn)
my_t = (mu-8)/(sd/sqn)
x[0]
#Tstat = 21.76, p-va;ue = 1.09, 
#Fail to reject HO