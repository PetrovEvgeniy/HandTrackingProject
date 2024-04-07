import math
from pathlib import Path
import cv2
import time
import numpy as np
import HandTrackingModule as htm


################################################################
widthCam, heightCam = 1280, 720
################################################################

# Load the image
image_path = Path("image.jpg")  # Set the path to the image file
img_original = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)

# Resize the image to match the video feed resolution
img_original = cv2.resize(img_original, (heightCam, heightCam))

# Resize the original image to the desired size
resize_factor = 0.3
img_resized = cv2.resize(img_original, (0, 0), fx=resize_factor, fy=resize_factor)

# Convert resized image to BGR format (3 channels)
img_resized_bgr = cv2.cvtColor(img_resized, cv2.COLOR_RGBA2BGR)

cap = cv2.VideoCapture(0)
cap.set(3, widthCam)
cap.set(4, heightCam)
previousTime = 0

handDetector = htm.handDetector(detectionCon=0.75)

activationThreshold = 25 # Set the activation threshold to 100

while True:
    success, img = cap.read()
    img = handDetector.findHands(img, draw=False) # Find the hands in the image
    lmList = handDetector.findPosition(img, draw=False) # Find the position of the landmarks in the image
    
    if len(lmList) != 0:
        #print(lmList[4]) # Print the position of the landmark at index 4
        #print(lmList[8]) # Print the position of the landmark at index 8
        #print(lmList[12]) # Print the position of the landmark at index 12
        
        # Get the positions of the landmarks at index 4, 8, and 12
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[12][1], lmList[12][2]
        
        # Draw a circle at the position of the landmarks
        # cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
        
        # # Draw a line between the landmarks
        # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
        # cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 3)
        # cv2.line(img, (x1, y1), (x3, y3), (0, 0, 255), 3)
        
        # Calculate the lengths of the formed triangle
    
        a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
        c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

        # Print the lengths of the sides on one line
        #print(f"Lengths of sides (a, b, c): {a:.2f}, {b:.2f}, {c:.2f}")
        
        
        # Calculate the center of the triangle
        center_x = (x1 + x2 + x3) / 3
        center_y = (y1 + y2 + y3) / 3

        # Calculate the position to place the resized image at the center of the triangle
        img_x = int(center_x - img_resized.shape[1] / 2)
        img_y = int(center_y - img_resized.shape[0] / 2) - 100

        # Print the coordinates of the center
        #print(f"Center of the triangle: ({center_x:.2f}, {center_y:.2f})")
        
        # Calculate the distances from the center to each of the points
        distance_to_p1 = math.sqrt((center_x - x1)**2 + (center_y - y1)**2)
        distance_to_p2 = math.sqrt((center_x - x2)**2 + (center_y - y2)**2)
        distance_to_p3 = math.sqrt((center_x - x3)**2 + (center_y - y3)**2)
        
        
        # Draw a circle at the center of the triangle only if the distance to each point is less than 100
        if distance_to_p1 < activationThreshold and distance_to_p2 < activationThreshold and distance_to_p3 < activationThreshold:
            # Overlay the resized image on the original image
            if img_x >= 0 and img_y >= 0:
                img[img_y:img_y+img_resized.shape[0], img_x:img_x+img_resized.shape[1]] = img_resized_bgr
            else:
                print("Resized image exceeds boundaries. Adjust the resize factor or triangle positions.")
            #cv2.circle(img, (int(center_x), int(center_y)), 15, (0, 255, 0), cv2.FILLED)
           
        
        
    
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 3)
        
    cv2.imshow("Image", img)
    
    # Wait for the user to press the 'Esc' key to exit the loop
    key = cv2.waitKey(1)
    if key == 27:  
        break