import cv2
import os
vidcap = cv2.VideoCapture(r"C:\Users\user\Downloads\WhatsApp Video 2021-09-10 at 09.46.15.mp4")
_dir = os.getcwd()   
_dir = os.path.join(_dir, input())
if not os.path.exists(_dir):
    os.makedirs(_dir)

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*100)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(os.path.join(_dir , "im{}.jpg".format(count)), image)        # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1 #//it will capture image in each 1 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)