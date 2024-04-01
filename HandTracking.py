import cv2
import mediapipe as mp
import time

# Capture the video from the webcam
cap = cv2.VideoCapture(0)

# Get the drawing utility object
mpDraw = mp.solutions.drawing_utils

# Get the mediapipe hands object in order to detect the hands
mpHands = mp.solutions.hands

# Get the hands object
hands = mpHands.Hands()



while True:
    # Read the image from the webcam
    success, img = cap.read()
    
    # Convert the image to RGB format
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process the image to detect the hands and store the results in the results variable
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            # Draw the landmarks on the image 
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    # Show the image in a window
    cv2.imshow("Image", img)
    
    # Wait for the user to press the 'Esc' key to exit the loop
    key = cv2.waitKey(1)
    if key == 27:  
        break



