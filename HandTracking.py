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

previousTime = 0
currentTime = 0

while True:
    # Read the image from the webcam
    success, img = cap.read()
    
    # Convert the image to RGB format
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process the image to detect the hands and store the results in the results variable
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                
                h, w, c = img.shape # Get the height, width and channels of the image
                cx, cy = int(lm.x*w), int(lm.y*h)   # Get the x and y coordinates of the landmark
                
                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                
                # Draw the landmarks on the image
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, 
                                      mpDraw.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=3),
                                       mpDraw.DrawingSpec(color=(0,255,0), thickness=2))
        

    # Calculate the frame rate
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    
    # Display the frame rate on the image
    cv2.putText(img, str(int(fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 3)
    
    # Show the image in a window
    cv2.imshow("Image", img)
    
    
    # Wait for the user to press the 'Esc' key to exit the loop
    key = cv2.waitKey(1)
    if key == 27:  
        break



