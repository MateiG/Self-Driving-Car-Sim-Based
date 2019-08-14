import win32api as wapi
import time
import numpy as np

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = [0,0]
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
                if key == "A":
                        keys[0] = 1
                elif key == "D":
                        keys[1] = 1
                elif key == "P":
                        keys[0] = -1
    return np.array(keys)