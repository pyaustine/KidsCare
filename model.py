import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model

# read data
model_data = pd.read_csv("./dataset/model_data.csv")

# split data
X = model_data.drop(columns=['ASD_Traits'])
y = model_data['ASD_Traits']

# split data into 70% training set and 30% temporary set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()

X_train = scale(X_train)
X_test = scale(X_test)
y_train = scale(y_train)
y_test = scale(y_test)


# Build and compile the ANN model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model on the training data
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# evaluate the model on testing data
ann_loss = model.evaluate(X_test, y_test, verbose=0)
print('ANN loss: ', ann_loss)

model.save('./savedModel/model.h5')