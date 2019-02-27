import numpy as np 
import cv2
import time
from get_screen import get_screen
from getkeys import key_check
import os
from directkeys import PressKey, ReleaseKey, W, A, S, D

from keras.models import load_model

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(W)

def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKeyD
    ReleaseKey(A)

def right():
    PressKey(D)
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def main():
    for i in list(range(2))[::-1]:
        print(i+1)
        time.sleep(1)
    last_time = time.time()

    #model = load_model('pygta5-car-0.001-DL-5-epochs.model')
    while True:
        screen = get_screen()

if __name__ == '__main__':
    main()