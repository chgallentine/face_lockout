# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2019-03-01 15:54:14
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2019-03-01 16:42:38
import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

while True:
	camera = cv2.VideoCapture(0)
	time.sleep(1)
	return_value, image = camera.read()
	cv2.imwrite('capture.jpg', image)
	del(camera)

	img = cv2.imread('./capture.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

	cv2.waitKey(1000)
	cv2.imshow('img',img)
	cv2.waitKey(1000)
	cv2.destroyAllWindows()