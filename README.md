# keras-gta5
Self driving car in GTA5 made with Keras on tensorflow backend. 
It is based on taking a image of the screen aswell as the players action as training data and label. It is not reccomended at the moment to use it in the city, but it performs really well on the highway going around the map.

It is greatly inspired by [this](https://www.youtube.com/watch?v=ks4MPfMq8aQ) fantastic video series by [Sentdex](https://github.com/Sentdex).

### Prerequisites

```
Python3
Numpy
Pandas
opencv
ctypes
Pillow
pywin32
keras
tensorflow
sklearn
```

## How to run:
Open GTA5 with a 800x600 resolution and drag it to the top left of the screen. 

Run gather_data.py and start collecting training data. The images plus label will be saved every 500 frames to training_data.npy

Then, run balance_data.py to reduce bias against driving straight forward. A new numpy file will be created called training_data_balanced_X.npy which cointains the balanced data. 

To train the CNN, run train_model_resnet.py, It will output a h5 files which contains the model and its weights. 

To unleash the AI in Los Santos, run predict.py. It will start a countdown and then start predicting and pressing the predicted buttons. To pause the prediction, 'T' can be pressed. 'R' will reset the counter showing the distrobution of the predicted actions.

## Comments

To train the CNN, a powerful GPU is a must. Training times on a GTX 1070 TI 8GB is around 1 hour on 150 000 images. 

## To do:
* Add video showcasing performance
* Work on quality of code
* Create setup.py
* Upload weights and training data
* Generalize to other racing games
