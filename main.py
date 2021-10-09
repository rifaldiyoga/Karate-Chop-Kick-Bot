import keyboard
import pyautogui

import numpy as np
import cv2
from time import time, sleep
from mss import mss

keyboard.wait("s")

branch_left = cv2.imread("branch_left.png")
branc_right = cv2.imread("branch_right.png")
branch_img = branch_left

SCT = mss()
left_dimensions = {'left': 1300, 'top': 510, 'width': 180, 'height': 200}
right_dimensions = {'left': 1650, 'top': 510, 'width': 180, 'height': 200}
isLeft = True
xx = 1500


# pyautogui.click(1650, 600)
fps_time = time()
while True:
    if(isLeft):
        img = np.array(SCT.grab(left_dimensions))
        branch_img = branch_left
    else:
        img = np.array(SCT.grab(right_dimensions))
        branch_img = branc_right

    scr_remove = img[:, :, :3]

    result = cv2.matchTemplate(scr_remove, branch_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    w = branch_img.shape[1]
    h = branch_img.shape[0]
    threshold = .60

    if max_val > threshold:
        print(f"Max Val : ", max_val)
        if(isLeft):
            isLeft = False
            xx = 1650
        else :
            isLeft = True
            xx = 1500
        cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)

    cv2.imshow('Screen Shot', img)
    cv2.waitKey(1)
    # print(xx)
    pyautogui.click(xx, 600)
    sleep(.06)
    #close window/
    if keyboard.is_pressed('q'):
        cv2.destroyAllWindows()
        start = False
        break