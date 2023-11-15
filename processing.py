# libraries
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import roc_curve, roc_auc_score, auc


# load data
data = pd.read_csv("./dataset/data.csv")

# data cleaning
# renaming columns
data.rename(columns={'Class/ASD Traits ': 'ASD_Traits'}, inplace=True)
data.rename(columns={'Who completed the test': 'Test completed by'}, inplace=True)

# Drop unnecessary colums
data.drop(columns=['Case_No'], inplace=True)

# Convert 'Ethnicity' and "Who completed the test" values to lowercase
data['Ethnicity'] = data['Ethnicity'].str.lower()
data['Test completed by'] = data['Test completed by'].str.lower()

# Replace 'm' with 'Male' and 'f' with 'Female' in the 'Sex' column
data['Sex'] = data['Sex'].replace({'m': 'Male', 'f': 'Female'})

# copy for further preprocessing
cleaned_data = data.copy()

# Encoding
# Sex Male=1, Female=0
# Jaundice Yes=1, No=0
cleaned_data['Sex'] = cleaned_data['Sex'].replace({'Female': 0, 'Male': 1})
cleaned_data['Jaundice'] = cleaned_data['Jaundice'].replace({'no': 0, 'yes': 1})
cleaned_data['Family_mem_with_ASD'] = data['Family_mem_with_ASD'].replace({'no': 0, 'yes': 1})
cleaned_data['ASD_Traits'] = cleaned_data['ASD_Traits'].replace({'No': 0, 'Yes': 1})

# Columns to one-hot encode
categorical_columns = ['Ethnicity', 'Test completed by']

# Create one-hot encoded DataFrames for the selected columns
one_hot_encoded = pd.get_dummies(cleaned_data[categorical_columns])

# Drop the original categorical columns
cleaned_data = cleaned_data.drop(columns=categorical_columns)

# Concatenate the one-hot encoded columns with the original data
cleaned_data = pd.concat([cleaned_data, one_hot_encoded], axis=1)

# Reorder columns so that 'ASD_Traits' is the last column
column_order = [col for col in cleaned_data.columns if col != 'ASD_Traits'] + ['ASD_Traits']
cleaned_data = cleaned_data[column_order]


# make a copy of the data for modelling
model_data = cleaned_data.copy()

# save the data as a csv
model_data.to_csv('./dataset/model_data.csv',index=False)