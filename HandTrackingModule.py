import cv2
import mediapipe as mp
import time

# Hand Detector Class - This class will be used to detect the hands in the image
class handDetector():
    
    # Constructor 
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        # Get the hands object in order to detect the hands
        self.mpHands = mp.solutions.hands
        
        # Store the hands object in the hands variable
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        
        # Get the drawing utility object
        self.mpDraw = mp.solutions.drawing_utils
    
    # Function to find the hands in the image and draw the landmarks on the image if the draw parameter is set to True
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw: # Draw the landmarks on the image if the draw parameter is set to True
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS, 
                                      self.mpDraw.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=3),
                                       self.mpDraw.DrawingSpec(color=(0,255,0), thickness=2))
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        lmList = [] # List to store the landmarks
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy]) # Append the landmark id, x and y coordinates to the list
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        
        return lmList



def main():
    
    cap = cv2.VideoCapture(0) # Capture the video from the webcam
    detector = handDetector() # Create an object of the handDetector class
    previousTime = 0
    currentTime = 0

    while True:
        success, img = cap.read() # Read the image from the webcam
        img = detector.findHands(img)
        
        lmList = detector.findPosition(img, handNo = 0, draw=False)
        
        if len(lmList) != 0:
            print(lmList[0])
        
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



if __name__ == '__main__':
    main()