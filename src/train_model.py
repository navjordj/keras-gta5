import numpy as np 

import datetime
from keras.utils import to_categorical

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.optimizers import SGD



train = np.load('training_data_balanced3.npy')
HEIGHT, WIDTH = 60, 80
X = []
y = []

for i in range(len(train)):
    X.append(train[i][0])
    y.append(train[i][1])

X = np.array(X)
y = np.array(y)

print([1, 0, 0] in y)

X = X.reshape(-1, HEIGHT, WIDTH, 1)
print(X.shape)

X = X.astype('float32')
X /=255

model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3), input_shape = (HEIGHT, WIDTH, 1), data_format="channels_last"))
model.add(Conv2D(32, kernel_size = (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))


print(model.output_shape)

sgd = SGD(lr=0.1)

model.compile( loss = "categorical_crossentropy", 
               optimizer = 'Adadelta', 
               metrics=['accuracy']
             )

history = model.fit(X, y, 
          batch_size=32, nb_epoch=25, verbose=1, validation_split=0.3)

model.save('{}-model-v14.h5'.format('test'))
