# Face Tracking Camera
Face-Tracking camera Arduino project that keeps a detected face centralized on the camera. It benefits from the OpenCV library on Python, and uses Arduino for controlling the two microservos used.

System build around OpenCV library on Python that detects faces from a webcam feed. The position of the face is transmitted to an Arduino, which processes the offset values and applies a proportional (P) control algorithm to drive two microservos. The servos rotate the camera platform in the horizontal and vertical axis, allowing the camera to continuously follow and center the detected face.

# Microservo Detailed Control System
Python code using OpenCV detects faces within the webcam feed and determines their positions in the image. When multiple faces are detected, the system selects a target based on the area of each detected face, prioritizing the largest face in the frame. The program then calculates the X (horizontal), and Y (vertical) pixel offsets between the face center and image center. These offsets represent the error values in the X and Y axes. The error values are transmitted to an Arduino through serial communication. A proportional (P) controller is applied to each value, controlling the pan and tilt servos. This allows the camera to adjust its orientation and keep the target face in the center of the frame.

# P controller
The controller output is calculated as:

A = K * e

(e) = error value (pixel offset)
(K) = Proportional constant
(A) = input to the servo (angle)

# Features
- Face detection using OpenCV library
- Arduino and Python communication
- Two axis control mechanism using microservos
- Movement smoothing
- Face choosing algorithm
- Draws rectangeles on the detected faces for easy debugging

# Materials used
- Arduino UNO
- Two SG90 Microservos
- Cardboard support
- 9v Battery
- Webcam

# Programs used
- Arduino IDE
- Python

# Future improvements
- Better servo and camera support
- Object detection
- Movement smoothing using D control
