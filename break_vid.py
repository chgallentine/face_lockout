# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2019-03-01 17:00:53
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2019-03-02 17:04:44
import cv2
import os

vidcap = cv2.VideoCapture('charlie.mp4')
success,image = vidcap.read()
count = 0

while success:
	cv2.imwrite(os.path.join("./dataset/charlie_gallentine/" , "{}.jpg".format(
			str(count).zfill(5))), image)    
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1