from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
import numpy as np
from keras.src.layers import LSTM
from keras.src.utils import to_categorical
from sklearn.model_selection import train_test_split


# Assuming 'data' is your input array of shape (371, 9, 250000)
def lstm(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

    input_shape = X_train.shape[1]

    model = Sequential()
    model.add(Dense(64, input_shape=(input_shape,), activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(8, activation='softmax'))  # 'num_classes' is the number of classes

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

def lstm1(data, labels):
    num_classes = 36  # Example number of classes, replace with your actual number

    model = Sequential()
    model.add(Dense(64, input_shape=(np.shape(data)[1],), activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))  # Output layer for multiclass classification

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    history = model.fit(data, labels, epochs=1000, batch_size=32, validation_split=0.2)

    return history.history['accuracy'], history.history['loss']

def lstm_deep(data, labels):
    model = Sequential()
    model.add(LSTM(64, input_shape=(np.shape(data)[1], np.shape(data)[2])))  # LSTM layer with 64 units
    model.add(Dense(1, activation='linear'))  # Output layer for regression, use proper activation

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])  # Use suitable loss for your problem

    # Train the model
    history = model.fit(data, labels, epochs=100, batch_size=32, validation_split=0.2)

    return history.history['loss']