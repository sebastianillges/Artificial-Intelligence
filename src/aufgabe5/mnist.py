import tensorflow as tf
from keras.src.layers import BatchNormalization

if not tf.__version__.startswith('2'):  # Checking if tf 2.0 is installed
    print('Please install tensorflow 2.0 to run this notebook')
import numpy as np

np.set_printoptions(linewidth=np.inf)
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Convolution2D, MaxPooling2D, Flatten, Activation
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import optimizers
from tensorflow.keras.datasets import mnist
from keras.callbacks import History
from keras.optimizers import Adam


def plot_history(hist, name, subplot_index, total_subplots):
    plt.subplot(total_subplots, 2, subplot_index)
    plt.plot(hist.history['accuracy'], linestyle='dotted', color='white')
    plt.plot(hist.history['val_accuracy'], color='blue')
    plt.title(f'{name} accuracy ({hist.history["accuracy"][-1]:.3f},{hist.history["val_accuracy"][-1]:.3f})',
              color='white')
    plt.ylabel('accuracy', color='white')
    plt.xlabel('epoch', color='white')
    plt.legend(['train', 'valid'], loc='lower right', facecolor='black')

    plt.subplot(total_subplots, 2, subplot_index + 1)
    plt.plot(hist.history['loss'], linestyle='dotted', color='white')
    plt.plot(hist.history['val_loss'], color='blue')
    plt.title(f'{name} loss ({hist.history["loss"][-1]:.3f},{hist.history["val_loss"][-1]:.3f})', color='white')
    plt.ylabel('loss', color='white')
    plt.xlabel('epoch', color='white')
    plt.legend(['train', 'valid'], loc='upper right', facecolor='black')



def eval_model(model, history, names, cnn=False):
    plt.style.use('dark_background')

    test_x = X_test_flat
    if cnn:
        test_x = X_test
    
    if isinstance(history, History):
        plt.figure(figsize=(12, 4))
        plt.title()
        plot_history(history, names[0], 1, 1)
        plt.tight_layout()
        plt.show()
        pred=model[0].predict(test_x )
        print(confusion_matrix(np.argmax(Y_test,axis=1),np.argmax(pred,axis=1)))
        acc_fc_orig = np.sum(np.argmax(Y_test,axis=1)==np.argmax(pred,axis=1))/len(pred)
        print("Accuracy = " , acc_fc_orig)
    elif isinstance(history, list) and all(isinstance(item, History) for item in history):
        num_histories = len(history)
        if len(names) != num_histories:
            raise ValueError("Die Anzahl der Namen muss der Anzahl der History-Objekte entsprechen.")
        plt.figure(figsize=(12, 4 * num_histories))
        for i, hist in enumerate(history):
            plot_history(hist, names[i], 2 * i + 1, num_histories)
            pred=model[i].predict(test_x )
            print(confusion_matrix(np.argmax(Y_test,axis=1),np.argmax(pred,axis=1)))
            acc_fc_orig = np.sum(np.argmax(Y_test,axis=1)==np.argmax(pred,axis=1))/len(pred)
            print(f"Accuracy of ", names[i], "= " , acc_fc_orig)
        plt.tight_layout()
        plt.show()
    else:
        raise ValueError("Die Eingabe muss entweder ein History-Objekt oder eine Liste von History-Objekten sein.")


print(
    "=============================================== Load Dataset =========================================================")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# separate x_train in X_train and X_val, same for y_train
X_train = x_train[0:50000] / 255  # divide by 255 so that they are in range 0 to 1
Y_train = keras.utils.to_categorical(y_train[0:50000], 10)  # one-hot encoding

X_val = x_train[50000:60000] / 255
Y_val = keras.utils.to_categorical(y_train[50000:60000], 10)

X_test = x_test / 255
Y_test = keras.utils.to_categorical(y_test, 10)

del x_train, y_train, x_test, y_test

print(f"X_train shape before reshape: {X_train.shape}")
X_train = np.reshape(X_train, (X_train.shape[0], 28, 28, 1))
print(f"X_train shape after reshape: {X_train.shape}")

print(f"X_val shape before reshape: {X_val.shape}")
X_val = np.reshape(X_val, (X_val.shape[0], 28, 28, 1))
print(f"X_val shape after reshape: {X_val.shape}")

print(f"X_test shape before reshape: {X_test.shape}")
X_test = np.reshape(X_test, (X_test.shape[0], 28, 28, 1))
print(f"X_test shape after reshape: {X_test.shape}")

print(X_train.shape)
print(X_val.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_val.shape)
print(Y_test.shape)

# print(
#     "======================================== Plotting the first 4 images =================================================")
# plt.figure(figsize=(12, 12))
# for i in range(0, 4):
#     plt.subplot(1, 4, (i + 1))
#     plt.imshow((X_train[i, :, :, 0]), cmap="blue")
#     plt.title(f"true label: {np.argmax(Y_train, axis=1)[i]}")
#     # plt.axis('off')
# plt.show()

print(
    "================================ fcNN as classification model for MNIST data =========================================")
print(
    "----------------------------- prepare data for fcNN - we need a vector as input --------------------------------------")
X_train_flat = X_train.reshape([X_train.shape[0], 784])
X_val_flat = X_val.reshape([X_val.shape[0], 784])
X_test_flat = X_test.reshape([X_test.shape[0], 784])

# check the shape
print(X_train_flat.shape)
print(Y_train.shape)
print(X_val_flat.shape)
print(Y_val.shape)

print(
    "---------------------------------------- define and train the fcNN model ---------------------------------------------")
# define fcNN with 2 hidden layers
model_sigmoid3 = Sequential()

model_sigmoid3.add(Dense(100, input_shape=(784,)))
model_sigmoid3.add(Activation('sigmoid'))
model_sigmoid3.add(Dense(50))
model_sigmoid3.add(Activation('sigmoid'))
model_sigmoid3.add(Dense(10))
model_sigmoid3.add(Activation('softmax'))

# compile model and intitialize weights
model_sigmoid3.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# summarize model along with number of model weights
model_sigmoid3.summary()

# train the model
history_sigmoid3 = model_sigmoid3.fit(X_train_flat, Y_train, batch_size=128, epochs=10, verbose=2,
                                      validation_data=(X_val_flat, Y_val))

print(
    "-------------------------------------------- plot the fcNN model -----------------------------------------------------")
# plot the development of the accuracy and loss during training
# eval_model(history_sigmoid3, "fcNN sigmoid 3 layers")

print(
    "----------------------------------------- evaluate the fcNN model ----------------------------------------------------")
pred = model_sigmoid3.predict(X_test_flat)
print(confusion_matrix(np.argmax(Y_test, axis=1), np.argmax(pred, axis=1)))
acc_fc_orig = np.sum(np.argmax(Y_test, axis=1) == np.argmax(pred, axis=1)) / len(pred)
print("Acc_fc_orig_flat = ", acc_fc_orig)

print(
    "========================================== Exercise: Improved fcNN ==================================================")
model_relu3 = Sequential()

model_relu3.add(Dense(100, input_shape=(784,)))
model_relu3.add(Activation('relu'))
model_relu3.add(Dense(50))
model_relu3.add(Activation('relu'))
model_relu3.add(Dense(10))
model_relu3.add(Activation('softmax'))

model_relu3.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model_relu3.summary()

history_relu3 = model_relu3.fit(X_train_flat, Y_train, batch_size=128, epochs=10, verbose=2,
                                validation_data=(X_val_flat, Y_val))

model_relu4 = Sequential()
model_relu4.add(Dense(100, input_shape=(784,)))
model_relu4.add(Activation('relu'))
model_relu4.add(Dense(50))
model_relu4.add(Activation('relu'))
model_relu4.add(Dense(25))
model_relu4.add(Activation('relu'))
model_relu4.add(Dense(10))
model_relu4.add(Activation('softmax'))

model_relu4.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model_relu4.summary()

history_relu4 = model_relu4.fit(X_train_flat, Y_train, batch_size=128, epochs=10, verbose=2,
                                validation_data=(X_val_flat, Y_val))

model_relu5 = Sequential()
model_relu5.add(Dense(200, input_shape=(784,)))
model_relu5.add(Activation('relu'))
model_relu5.add(Dense(100))
model_relu5.add(Activation('relu'))
model_relu5.add(Dense(50))
model_relu5.add(Activation('relu'))
model_relu5.add(Dense(25))
model_relu5.add(Activation('relu'))
model_relu5.add(Dense(10))
model_relu5.add(Activation('softmax'))

model_relu5.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model_relu5.summary()

history_relu5 = model_relu5.fit(X_train_flat, Y_train, batch_size=128, epochs=10, verbose=2,
                                validation_data=(X_val_flat, Y_val))

eval_model([history_sigmoid3, history_relu3, history_relu4, history_relu5],
           ["sigmoid 3 layers", "relu 3 layers", "relu 4 layers", "relu 5 layers"])

print("Aufgabe 1:")
print(
    "Exercise: Try to improve the fcNN by adding more hidden layers and/or changing the activation function from\
    'sigmoid' to 'relu'. What do you observe? can you improve the performace on the testset?\n")
print("Answer:")
print("Changing the activation function from sigmoid to relu has a positive effect on the performance of the model.\n\
      Especially on the accuracy of the training data and a bit on the validation data.\n\
      The more hidden layers we add, the more unstable does the model get. Also the accuracy is not improved.\n\
      Also increasing the number of epochs has a negative effect on all models using the relu function.")




model_cnn = Sequential()
model_cnn.add(Input(shape=(28,28,1)))
model_cnn.add(Convolution2D(32, 3, padding="same"))
model_cnn.add(MaxPooling2D(pool_size=2))
model_cnn.add(Convolution2D(64, 3))
model_cnn.add(MaxPooling2D(pool_size=2))
model_cnn.add(Flatten())
model_cnn.add(Dense(10))
model_cnn.add(Activation("softmax"))

model_cnn.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model_cnn.summary()



print(X_train.shape)
history_cnn = model_cnn.fit(X_train, Y_train, batch_size=128, epochs=10, verbose=2,
                                validation_data=(X_val, Y_val))


eval_model([model_cnn], [history_cnn], ["cnn"], cnn=True)


