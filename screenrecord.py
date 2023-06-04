from PIL import ImageGrab
import numpy as np
import cv2



while True:
    img = ImageGrab.grab(bbox=(0,0,1280,720))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2BGR555)
    

    cv2.imshow('Secret Capture', img_final)
    cv2.waitKey(10)