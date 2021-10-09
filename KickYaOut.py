import cv2
import mss
import numpy as np
import time
import os

class KickYaOut:

    def __init__(self):
        self.SCT = mss.mss()
        self.dimensions = {'left': 600, 'top': 110, 'width': 720, 'height': 960}


