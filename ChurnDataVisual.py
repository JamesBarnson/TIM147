# James Barnson
# TIM147 Data Mining for Business
# HW1: Customer Churn Data visualization
# 10/15/2023

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

# sns.set(style='ticks', palette='Paired')
#changing seaborn style
# plt.pyplot.show()

churn_df = pd.read_excel('Customer_Churn.xlsx')
# print('\n', churn_df.head(), '\n') #Show the first few lines of the data
# print('\n', churn_df.describe().round(3), '\n') #Show summary statistics of the data
# print(churn_df.info(), '\n') #show information about each column

# churn_df.hist('OVERAGE')
# plt.pyplot.show()
#Create and display a histogram to see shape of overage data

# sns.jointplot(data=churn_df, x='OVERAGE', y='INCOME', hue='LEAVE')
# plt.pyplot.show()
#Create and display a scatterplot and density curve joint plot
# comparing overages and income, with different colors for whether the customer
# left or stayed.

print('COLLEGE Categories:', churn_df['COLLEGE'].unique())
print('REPORTED_SATISFACTION Categories:', churn_df['REPORTED_SATISFACTION'].unique())
print('REPORTED_USAGE_LEVEL Categories:', churn_df['REPORTED_USAGE_LEVEL'].unique()) 
print('CONSIDERING_CHANGE_OF_PLAN Categories:', churn_df['CONSIDERING_CHANGE_OF_PLAN'].unique())
print('LEAVE Categories:', churn_df['LEAVE'].unique(), '\n')
