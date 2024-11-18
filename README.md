# Count-With-Me

## AI Finger Counter: Real-Time Finger Counting Using Mediapipe
This project is a real-time AI-powered finger counter that uses a webcam to detect and count the number of fingers shown on one or both hands. It leverages Mediapipe Hands, a robust hand-tracking solution, and OpenCV for video processing and display.

## Features
Detects up to 4 hands simultaneously.
Counts fingers individually for both left and right hands.
Displays the total finger count on the video feed.
Real-time detection with flip-mirror functionality for user-friendly interaction.
Highly customizable and easy to extend.
## How It Works
Hand Detection: Mediapipe's Hands module detects hand landmarks in the video feed.
Landmark Analysis: A custom count function determines which fingers are raised using landmark positions.
Handedness Detection: The program distinguishes between left and right hands to accurately count thumbs.
Output: The total count of fingers across all detected hands is displayed on the video feed.
## Code Breakdown
1. Dependencies
OpenCV: For accessing the webcam and processing video frames.
Mediapipe Hands: For detecting hand landmarks and determining handedness.
Matplotlib (Optional): For debugging or displaying frames.
2. Key Functions
get_landmark(): Extracts hand landmark coordinates into a list for easier analysis.
count(): Determines how many fingers are raised based on landmark positions, with specific logic for left and right hands.
3. Main Program
Captures video from the webcam using OpenCV.
Processes each frame to detect hands and count fingers in real time.
Displays the count as an overlay on the video feed.
Press 'q' to exit the program.
## Customization
Adjust max_num_hands in the Hands object to detect fewer or more hands.
Modify the count function to experiment with different hand gestures or rules.
## Applications
Interactive games.
Gesture-based controls for devices.
Educational tools for teaching numbers or gestures.
