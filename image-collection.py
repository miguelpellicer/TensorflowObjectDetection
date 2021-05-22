import cv2
import uuid
import os
import time
import sys


def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)


labels = ['one', 'two', 'three', 'four', 'five']
number_imgs = sys.argv[1]

IMAGES_PATH = os.path.join('images', 'training')
createFolder(IMAGES_PATH)

for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    createFolder(path)

    cap = cv2.VideoCapture(0)  # CONNECTS TO WEBCAM (if error, change port)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label +'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
