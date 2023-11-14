import pandas as pd
import tensorflow as tf
from tensorflow import keras

# read data
model_data = pd.read_csv('./dataset/model_data.csv')

# split data
X = model_data.drop(columns=['ASD_Traits'])
y = model_data['ASD_Traits']