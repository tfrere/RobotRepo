from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2
import picamera.array

camera = PiCamera()
camera.resolution = (800, 600)
camera.framerate =10
rawCapture = PiRGBArray(camera, size=(800, 600))

time.sleep(0.1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
	img = frame.array
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)

	if key == ord("q"):
				break
	

