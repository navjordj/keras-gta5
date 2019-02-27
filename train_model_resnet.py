import numpy as np 

import datetime
from keras.utils import to_categorical

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.optimizers import SGD

from sklearn.model_selection import train_test_split

HEIGHT, WIDTH = 60, 80

def main():
    X = []
    y = []
    for i in range(len(train)):
        X.append(train[i][0])
        y.append(train[i][1])

    X = np.array(X)
    y = np.array(y)

    plt.imshow(X[0])
    plt.show()

    X = X.reshape(-1, HEIGHT, WIDTH, 1) 

    X = X.astype('float32')
    X /=255

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(HEIGHT, WIDTH, 1)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax'))

    sgd = SGD(lr=0.0001, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    history = model.fit(X_train, y_train, batch_size=32, epochs=25, verbose = 1)
    print("Evaluerer:")
    print(model.evaluate(X_train, y_train, batch_size=32, verbose=1))

    model.save('{}-model-v14.h5'.format('test'))

if __name__ == '__main__':
    Navn = 'training_data_balanced6.npy'
    try:
        train = np.load(Navn)
    except:
        print("{} ikke funnet".format(Navn))
    main()
