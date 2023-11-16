import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Read data
model_data = pd.read_csv("./dataset/model_data.csv")

# Changing column names to lowercase
model_data.columns = map(str.lower, model_data.columns)
print('----Columns renamed successfully---')

# Rename column
model_data.rename(columns={'family_mem_with_asd': 'asd_history'}, inplace=True)
model_data.rename(columns={'asd_traits': 'outcome'}, inplace=True)

# Drop column
model_data.drop(columns=['test completed by_self'], inplace=True)

# Create a new column based on the conditions
model_data['test_completed_by'] = np.where(
    (model_data['test completed by_family member'] == 1) | (model_data['test completed by_health care professional'] == 1),
    1,  # Value for ('Test_completed_by_family member' and 'Test_completed_by_health care professional')
    0   # Value for 'Test_completed_by_others'
)

# Drop the original columns if needed
model_data = model_data.drop(['test completed by_family member', 'test completed by_health care professional', 'test completed by_others'], axis=1)

print('--------New column created successfully----------')

# Print column names
print(model_data.columns)

# Scale
cols_to_scale = ['age']
scaler = MinMaxScaler()
model_data[cols_to_scale] = scaler.fit_transform(model_data[cols_to_scale])

# Split data
X = model_data.drop(columns=['outcome'])
y = model_data['outcome']

# Convert outcome to 0 or 1
y = y.astype(int)

# Split data into 70% training set and 30% temporary set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build and compile the ANN model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model on the training data
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model on the testing data
ann_accuracy = model.evaluate(X_test, y_test)
print("ANN Accuracy:", ann_accuracy)

# Save the model
model.save('./savedModel/model.h5')

print('-----------Model fit and saved successfully-----------------')
