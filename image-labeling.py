import cv2
import uuid
import os
import time
import sys

LABELIMG_PATH = os.path.join('resources', 'labelImg')
ABSOLUTE_LABELIMG_PATH = os.path.join(os.getcwd(), LABELIMG_PATH)
if not os.path.exists(LABELIMG_PATH):
    os.mkdir(LABELIMG_PATH)
    os.system('git clone https://github.com/tzutalin/labelimg ' + LABELIMG_PATH)

if os.name == 'posix':
    os.system('cd' + ABSOLUTE_LABELIMG_PATH + '&& make qt5py3')
if os.name == 'nt':
    os.system('cd ' + ABSOLUTE_LABELIMG_PATH +' && pyrcc5 -o libs/resources.py resources.qrc')

os.system('cd ' + ABSOLUTE_LABELIMG_PATH + ' && python labelImg.py')