from screen_grab import record
from get_keys import key_check
import cv2
import numpy as np
import time
import os

paused = False
training_data = []
while True:
    keys = key_check()
    print(keys)
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
        screen = record((0,0,640,400))
        resized = cv2.resize(screen,(40,25))
        training_data.append([resized,keys])
        if len(training_data) % 500 == 0:
            np.save("new_training/" + str(time.time()), training_data)
            training_data = []
        cv2.imshow('frame',resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break