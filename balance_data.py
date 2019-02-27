import numpy as np 
import pandas as  pd 
from collections import Counter
from random import shuffle

import cv2


def main():

    df = pd.DataFrame(train_data)

    print(Counter(df[1].apply(str))) #finne ut hvor fordelt dataen er.

    left = []
    right = []
    forward = []

    shuffle(train_data)
    for data in train_data:
        img = data[0]
        choice = data[1]
        if choice == [1, 0, 0]:
            left.append([img, choice])
        elif choice == [0, 1, 0]:
            forward.append([img, choice])
        elif choice == [0, 0, 1]:
            right.append([img, choice])
        else:
            print("ingen valg")

    print(len(left), len(forward), len(right))
    lengths = [len(left), len(forward), len(right)]
    minValue = np.argmin(lengths)

    print(minValue)
    forward = forward[:int(2*lengths[minValue])]
    left = left[:lengths[minValue]]
    right = right[:lengths[minValue]]

    final_data = forward + right + left
    shuffle(final_data)
    print(len(final_data))

    np.save('training_data_balanced6.npy', final_data)

if  __name__ == "__main__":
    name = 'training_data.npy'
    try:
        train_data = np.load(name)
    except:
        print("{} ikke funnet".format(name))
    main()