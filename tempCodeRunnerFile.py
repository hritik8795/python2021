import cv2

cam =cv2.VideoCapture(1)
while cam.isOpened():
    ret,frame =cam.read()
    cv2.imshow('Granny cam ,frame')