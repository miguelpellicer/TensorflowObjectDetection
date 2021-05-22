import cv2
import uuid
import os
import time
import sys

LABELING_PATH = os.path.join('resources', 'labelImg')
if not os.path.exists(LABELING_PATH):
    os.mkdir(LABELING_PATH)
    os.system('git clone https://github.com/tzutalin/labelimg '+LABELING_PATH)
