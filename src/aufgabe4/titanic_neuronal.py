import tensorflow as tf
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Daten laden und vorbereiten
train_data = pd.read_csv("data/train.csv")
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median(skipna=True))
train_data = pd.get_dummies(train_data[["Pclass", "Survived", "Sex", "Age"]])
train_data.info()
print(train_data)

x = train_data.drop('Survived', axis=1, inplace=False)
y = train_data['Survived']

print(x)
print(y)

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)
x_train = np.asarray(x_train).astype('float32')
x_val = np.asarray(x_val).astype('float32')
y_train = np.asarray(y_train).astype('float32')
y_val = np.asarray(y_val).astype('float32')

# Modell definieren
model = Sequential()
model.add(Dense(8, activation='sigmoid', input_shape=(4,)))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

# Modell kompilieren
opt = tf.keras.optimizers.Adam(learning_rate=1e-3)
model.compile(loss=tf.keras.losses.BinaryCrossentropy(),
              optimizer=opt,
              metrics=['accuracy'])

model.summary()

# Modell trainieren
history = model.fit(x_train, y_train, epochs=50, batch_size=32, validation_data=(x_val, y_val))

# Modell evaluieren
model.evaluate(x_val, y_val)

# Plotten der Loss-Kurven
plt.plot(history.history['loss'], label='Trainingsverlust')
plt.plot(history.history['val_loss'], label='Validierungsverlust')
plt.xlabel('Epoche')
plt.ylabel('Verlust')
plt.legend()
plt.show()
