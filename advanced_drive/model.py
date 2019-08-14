import numpy as np
from keras.layers import Dense, Activation, Flatten, Conv2D, Lambda
from keras.layers import MaxPooling2D, Dropout
from keras.utils import print_summary
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from keras.models import load_model

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def model(width, height, depth):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape = (width, height, depth)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D((2, 2), padding='valid'))
    model.add(Conv2D(32, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D((2, 2), padding='valid'))

    # model.add(Conv2D(64, (3, 3), padding='same'))
    # model.add(Activation('relu'))
    # model.add(MaxPooling2D((2, 2), padding='valid'))
    # model.add(Conv2D(64, (3, 3), padding='same'))
    # model.add(Activation('relu'))
    # model.add(MaxPooling2D((2, 2), padding='valid'))

    # model.add(Conv2D(128, (3, 3), padding='same'))
    # model.add(Activation('relu'))
    # model.add(MaxPooling2D((2, 2), padding='valid'))
    # model.add(Conv2D(128, (3, 3), padding='same'))
    # model.add(Activation('relu'))
    # model.add(MaxPooling2D((2, 2), padding='valid'))

    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(1024))
    model.add(Dense(256))   
    model.add(Dense(64))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss="mse")
    print(model.summary())
    return model

def load(path="cleaned.npy"):
    all = np.load(path, allow_pickle=True)
    features = []
    labels = []
    for pair in all:
        features.append(pair[0])
        labels.append(pair[1])
    return features, labels

def main(model, features, labels):
    train_x, test_x, train_y, test_y = train_test_split(features, labels, random_state=0, test_size=0.3)
    train_x = np.array(train_x)
    train_y = np.array(train_y)

    test_x = np.array(test_x)    
    test_y = np.array(test_y)
    return test_x, test_y
    # print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)
    # train_y = train_y.reshape(train_y.shape[0], 2, -1)
    # test_y = test_y.reshape(test_y.shape[0], 2, -1)
    # print(train_y.shape)
    # train_x = train_x.reshape(train_x.shape[0], width, height, depth, -1)
    # test_x = test_x.reshape(width, height, depth, -1)

    # model.fit(train_x, train_y, validation_data=(test_x, test_y), epochs=50, batch_size=32, verbose=True)
    # model.save('autopilot.h5')
model = load_model('autopilot.h5')
features, labels = load()
# model = model(12, 128, 4)
test_x, test_y = main("hello", features, labels)
print(model.evaluate(test_x, test_y))