import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

iris = load_iris()
X = iris.data         # Features: sepal/petal length & width (4 values)
y = iris.target       # Labels: 0, 1, 2 (setosa, versicolor, virginica)
y_encoded = to_categorical(y)  # Converts 0 → [1,0,0], 1 → [0,1,0], etc.

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(8, input_shape=(4,), activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

predictions = model.predict(X_test)
print(predictions)
#print(y_test)
predicted_classes = np.argmax(predictions, axis=1)
print(predicted_classes)
actual_classes = np.argmax(y_test, axis=1)
print(actual_classes)

import numpy as np
from sklearn.datasets import load_digits
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Step 1: Load the digits dataset
digits = load_digits()
X = digits.data  # Features (8x8 images flattened into 64 features)
y = digits.target  # Labels (0-9)

# Step 2: Preprocess the data
# Scale the features so that they are in the range [0, 1]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert labels to one-hot encoded format
y_one_hot = to_categorical(y, 10)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_one_hot, test_size=0.2, random_state=42)

# Step 3: Define the ANN model
model = Sequential()

# Input layer: Flatten the 64 features into 1D (though it's already 1D, so no need to reshape)
model.add(Dense(64, input_dim=64, activation='relu'))  # First hidden layer with 64 neurons
model.add(Dense(32, activation='relu'))  # Second hidden layer with 32 neurons
model.add(Dense(10, activation='softmax'))  # Output layer with 10 neurons for digits 0-9

# Step 4: Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 5: Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)

# Step 6: Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")

# Step 7: Make predictions
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
actual_classes = np.argmax(y_test, axis=1)

# Show some predictions
for i in range(5):
    print(f"Predicted: {predicted_classes[i]}, Actual: {actual_classes[i]}")
