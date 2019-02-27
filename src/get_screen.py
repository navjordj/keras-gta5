import numpy as np
from PIL import ImageGrab
import cv2
import time

from directkeys import PressKey, ReleaseKey, W, A, S, D


def get_screen(): 
    printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640))) #560,250,1360,850 for midt på skjermen
    #img = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
    return printscreen













