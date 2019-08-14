from screen_grab import record
from get_keys import key_check
import cv2
import numpy as np
import time
import os
from keras.models import load_model
from direct_keys import PressKey, ReleaseKey, W, A, S, D

model = load_model('autopilot.h5')
paused = False
while True:
    keys = key_check()
    if -1 in keys:
        if not paused:
            paused = True
            print("Pausing")
            time.sleep(1)
        else:
            print("Unpaused")
            paused = False
            time.sleep(1)
    if not paused:
        screen = record((0,230,640,290))
        resized = cv2.resize(screen,(128,12))
        pred = model.predict(resized.reshape(1, 12, 128, 4))[0][0]
        print(pred)
        # if pred < -0.1:
        #     print("left")
        #     PressKey(A)
        #     time.sleep(0.5)
        #     ReleaseKey(A)
        # elif pred > 0.1:
        #     print("right")
        #     PressKey(D)
        #     time.sleep(0.5)
        #     ReleaseKey(D)
        # top = np.where(pred[0] == np.amax(pred[0]))
        # if top[0] == 1:

        # elif top[0] == 0:
        #     PressKey(D)
        #     time.sleep(0.01)
        #     ReleaseKey(A)
        cv2.imshow('frame', resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break