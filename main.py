import keyboard
import pyautogui

import numpy as np
import cv2
from time import time, sleep
from mss import mss

keyboard.wait("s")

branch_left = cv2.cvtColor(cv2.imread("branch_left2.png"), cv2.COLOR_BGR2GRAY)
branc_right = cv2.cvtColor(cv2.imread("branch_right2.png"), cv2.COLOR_BGR2GRAY)


branch_img = branch_left

SCT = mss()
left_dimensions = {'left': 1400, 'top': 690, 'width': 180, 'height': 150}
right_dimensions = {'left': 1550, 'top': 690, 'width': 180, 'height': 150}
isLeft = True
xx = 1500

fps_time = time()
while True:
    if(isLeft):
        img = np.array(SCT.grab(left_dimensions))
        branch_img = branch_left
    else:
        img = np.array(SCT.grab(right_dimensions))
        branch_img = branc_right

    scr_remove = cv2.cvtColor(img[:, :, :3], cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(scr_remove, branch_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    # w = branch_img.shape[1]
    # h = branch_img.shape[0]
    threshold = .50

    if max_val > threshold:
        print(f"Max Val : ", max_val)
        if(isLeft):
            isLeft = False
            xx = 1650
        else :
            isLeft = True
            xx = 1500
        print(isLeft)
        # cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)

    # cv2.imshow('Screen Shot', img)
    # cv2.waitKey(1)
    pyautogui.click(xx, 600)
    sleep(.15)
    #close window/
    if keyboard.is_pressed('q'):
        cv2.destroyAllWindows()
        start = False
        break

    # print('FPS: {}'.format(1 / (time() - fps_time)))
    # fps_time = time()

#
# result = cv2.matchTemplate(bg_img, branch_img, cv2.TM_CCOEFF_NORMED)
#
# # cv2.imshow("tes",result)q
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
# print(max_val)
#
# w = branch_img.shape[1]
# h = branch_img.shape[0]
# threshold = .60
#
# yloc, xloc = np.where(result >= threshold)
#
# print(len(xloc))
#
# rectangles = []
# for (x, y) in zip(xloc, yloc):
#     rectangles.append([int(x), int(y), int(w), int(h)])
#     rectangles.append([int(x), int(y), int(w), int(h)])
#
#
# rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
#
# for (x, y) in zip(xloc, yloc):
#     cv2.rectangle(bg_img, (x, y), (x + w, y + h), (0,255,255), 2)
#
# cv2.imshow("tes",bg_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




