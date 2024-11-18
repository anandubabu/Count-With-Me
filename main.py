#importing necessary libraries
import cv2 as cv
import numpy as np
import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.drawing_utils as drawing
import matplotlib.pyplot as plt

# function to get landmark values in list
def get_landmark(l):
    landmark_list = []
    for i, landmark in enumerate(l):
        landmark_list.append([i, landmark.x, landmark.y])
    return landmark_list
#function to count fingers(for more details to get values visit hand landmark detection guide)
def count(landmark_list,left_hand):
    c = 0
    # count fingers based on y values
    if landmark_list[8][2] < landmark_list[6][2]:
        c += 1
    if landmark_list[12][2] < landmark_list[10][2]:
        c += 1
    if landmark_list[16][2] < landmark_list[14][2]:
        c += 1
    if landmark_list[20][2] < landmark_list[18][2]:
        c += 1
    # to check thumb values which is counted based on x values
    if left_hand:
        if landmark_list[2][1] < landmark_list[4][1]:#left hand thumb
            c += 1

    else:
        if landmark_list[2][1]>landmark_list[4][1]:#right hand thumb
            c+=1
        
    return c

# object for hand detection
hands = mpHands.Hands(static_image_mode=False, max_num_hands=4, min_detection_confidence=0.5)

# Camera accessing
cam = cv.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if not ret:
        print("Camera access denied...")
        break
    flip_frame = cv.flip(frame, 1)
    rgbframe = cv.cvtColor(flip_frame, cv.COLOR_BGR2RGB)
# hand detection and counting 
    d = hands.process(rgbframe)

    total = 0
    if d.multi_hand_landmarks and d.multi_handedness:
        finger = []#list to store values of opened fingers
        for landmarks, hand in zip(d.multi_hand_landmarks, d.multi_handedness):
        # Determine if the hand is left or right
            left_hand = hand.classification[0].label == "Left"
            landmark_list = get_landmark(landmarks.landmark)
            fc=count(landmark_list,left_hand)
            finger.append(fc)
            #print(fc)
        total = sum(finger) #sum of all opened fingers
        #print(total)
        cv.putText(flip_frame,str(total),(495,153),cv.FONT_HERSHEY_PLAIN,5,(0,0,0),10)#to write down the count
    else:
        print("No hands detected.")
        #cv.putText(flip_frame,'No Hand Detected',(150,100),cv.FONT_HERSHEY_PLAIN,3,(0,0,0),3)#to write down the count

    cv.imshow('Landmark', flip_frame)
    #plt.imshow(flip_frame) to get the values to show fingure count in screen
    #plt.show()

    if cv.waitKey(1) == ord('q'):# to stop the program we need to press q
        break

cam.release()
cv.destroyAllWindows()
