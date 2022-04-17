# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:06:44 2022

@author: Admin
"""

# example for variance_inflation_factor
import pandas as pd 
  
# the dataset
data = pd.read_csv('C:/Users/Admin/Downloads/BMI.csv')
  
# printing first few rows
print(data.head())

from statsmodels.stats.outliers_influence import variance_inflation_factor
  
# creating dummies for gender
data['Gender'] = data['Gender'].map({'Male':0, 'Female':1})
  
# the independent variables set
X = data[['Gender', 'Height', 'Weight']]
  
# VIF dataframe
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
  
# calculating VIF for each feature
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
  
print(vif_data)