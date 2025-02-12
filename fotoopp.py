'''
     Programação.....: (C) 2025. Diogo Ramiro
     Data............: 07/02/2025
     Observacoes.....:
'''

import cv2 as cv
import numpy as np

# Initialize webcam
webcam = cv.VideoCapture(0)

if not webcam.isOpened():
    print('Startup Error!')
    exit()

# Read the first frame
ret, previous_frame = webcam.read()
if not ret:
    print("Error capturing initial frame")
    webcam.release()
    exit()

previous_frame = cv.cvtColor(previous_frame, cv.COLOR_BGR2GRAY)
previous_frame = cv.GaussianBlur(previous_frame, (21, 21), 0)

while True:
    ret, frame = webcam.read()
    if not ret:
        print('Error capturing frame')
        break
    
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_frame = cv.GaussianBlur(gray_frame, (21, 21), 0)
    
    # Compute the absolute difference between frames
    frame_delta = cv.absdiff(previous_frame, gray_frame)
    
    # Apply threshold to highlight differences
    threshold = cv.threshold(frame_delta, 25, 255, cv.THRESH_BINARY)[1]
    threshold = cv.dilate(threshold, None, iterations=2)
    
    # Find contours of moving objects
    contours, _ = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv.boundingRect(contour)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv.imshow('Motion Detection', frame)
    cv.imshow('Threshold', threshold)
    
    previous_frame = gray_frame  # Update previous frame
    
    if cv.waitKey(1) == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()
