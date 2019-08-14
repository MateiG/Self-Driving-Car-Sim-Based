from screen_grab import record
from get_keys import key_check
import cv2
import numpy as np
import time
import os

paused = False
training_data = []
pre_time = time.time()
while True:
    keys = key_check()
    if -1 in keys:
        if paused:
            paused = False
            print("Unpaused")
            time.sleep(1)
        else:
            print("Pausing")
            paused = True
            time.sleep(1)
    if not paused:
        screen = record((0,230,640,290))
        resized = cv2.resize(screen,(128,12))
        training_data.append([resized,keys])
        print(keys)
        # if len(training_data) % 500 == 0:
        #     prev = np.load("new_training.npy", allow_pickle=True) if os.path.isfile("new_training.npy") else []
        #     np.save("new_training.npy", np.append(prev, training_data))
        #     training_data = []
        #     print(len(prev))
        cv2.imshow('frame', resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break