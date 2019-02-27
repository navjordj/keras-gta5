import numpy as np
import cv2

import time
import os

from PIL import ImageGrab

from directkeys import PressKey, ReleaseKey, W, A, S, D
from get_screen import get_screen
from getkeys import key_check

file_name = 'training_data.npy'

def keys_to_output(keys):
    """
    Tar listen med trykte knapper og 
    returnerer en liste med den trykte knappen
    """
    #[A, W, D]
    output = [0, 0, 0]
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output

def main():
    if os.path.isfile(file_name):
        print("Laster treningsdata")
        training_data = list(np.load(file_name))
    else:
        print("Generererer ny treningsdata")
        training_data = []

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    last_time = time.time()
    print("Lengde på treningsdata: {}".format(len(training_data)))
    print("Startet innsamling av treningsdata")
    while(True):
        screen = get_screen()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80, 60))

        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen, output])
        
        #print('Bildet tok {} sekunder. {} fps'.format(time.time() - last_time, 1/(time.time()-last_time)))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)
if __name__ == "__main__":
    main()