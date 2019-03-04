# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png 

# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import time
import os

data = pickle.loads(open("encodings.pickle", "rb").read())

camera = cv2.VideoCapture(0)
time.sleep(1)

while True:
	return_value, image = camera.read()
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	boxes = face_recognition.face_locations(rgb, model="hog")
	encodings = face_recognition.face_encodings(rgb, boxes)

	people = []

	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			name = max(counts, key=counts.get)
		
		people.append(name)

	if ("charlie_gallentine" not in people) and ("Unknown" in people):
		os.system("/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine")









