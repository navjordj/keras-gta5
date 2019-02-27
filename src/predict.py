import numpy as np
from get_screen import get_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from getkeys import key_check

from keras.models import load_model
import random

t_time = 0.04

def straight():
    PressKey(W)
    time.sleep(t_time)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(W)

def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(W)

    ReleaseKey(A)

def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(W)
    ReleaseKey(D)

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 10

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    L = 0
    R = 0
    S = 0

    while(True):
        
        if not paused:
            screen = get_screen()
            #print('loop took {} seconds'.format(time.time()-last_time)) #Printer tiden et bilde + prediction tok
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (HEIGHT ,WIDTH))
            
            prediction = model.predict([screen.reshape(1, HEIGHT ,WIDTH,1)])[0]
            #print(prediction)
            turn_thresh = 0.8
            fwd_thresh = 0.70

            if prediction[1] > fwd_thresh:
                S +=1
                straight()
            elif prediction[0] > turn_thresh:
                L +=1
                left()
            elif prediction[2] > turn_thresh:
                R +=1
                right()
            else:
                straight()
            print('{} L, {} S, {} R'.format(L, S, R))
        keys = key_check()

        if 'T' in keys: #T for å pause/starte 
            if paused:
                print("Begynner igjen")
                paused = False
                time.sleep(1)
            else:
                print("Pauser")
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)
        if 'R' in keys:
            L = 0
            R = 0
            S = 0

if __name__ == '__main__':
    Navn = 'test-model-v14.h5'
    try:
        print(Navn)
        model = load_model(Navn)
    except:
        print("{} ikke funnet".format(Navn))
    main()       
