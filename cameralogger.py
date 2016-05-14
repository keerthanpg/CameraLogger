import cv2
import datetime
import os
fp=open('ImageDateStamps.txt', 'a')
j=0

camera_port = 0 
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def get_image():
    
 retval, im = camera.read()
 return im

while(1):
    for i in xrange(ramp_frames):
        temp = camera.read()

    camera_capture = get_image()
    time=str(datetime.datetime.now())
    imagename =str(j)
    filename = "%s.jpg"%imagename
    cv2.imwrite(filename,camera_capture)
    fp.write("%s %s \n" %(imagename, time))
    j=j+1
#    if j>5:
#      break

del(camera)
fp.close()
