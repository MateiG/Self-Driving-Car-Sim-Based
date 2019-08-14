import numpy as np
import cv2
import glob
from random import shuffle
import pandas as pd
from collections import Counter

file_name = "new_training.npy"
loaded = np.load(file_name, allow_pickle=True)
all_data = []

for i in range(0, len(loaded), 2):
        all_data.append([loaded[i], loaded[i+1]])
shuffle(all_data)

left_imgs = []
right_imgs = []
straight_imgs = []

for pair in all_data:
        if pair[1] == [1,0]:
                left_imgs.append(pair[0])
        elif pair[1] == [0,1]:
                right_imgs.append(pair[0])
        else:
                straight_imgs.append(pair[0])

if len(left_imgs) < len(right_imgs):
        for i in range(len(right_imgs) - len(left_imgs)):
                vert = cv2.flip(right_imgs[i], 1)
                left_imgs.append(vert)
elif len(right_imgs) < len(left_imgs):
        for i in range(len(left_imgs) - len(right_imgs)):
                vert = cv2.flip(left_imgs[i], 1)
                right_imgs.append(vert)

straight_imgs = straight_imgs[:len(left_imgs)]
print(len(left_imgs), len(right_imgs), len(straight_imgs))

lefts = []
rights = []
straights = []
for img in left_imgs:
        lefts.append([img, -1])
for img in right_imgs:
        rights.append([img, 1])
for img in straight_imgs:
        straights.append([img, 0])
final = lefts + rights + straights


final = lefts + rights + straights

shuffle(final)
np.save("cleaned.npy", final)

for i in final:
        cv2.imshow('frame', i[0])
        print(i[1])
        if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break