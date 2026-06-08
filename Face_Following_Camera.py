import cv2
import serial

arduino = serial.Serial("COM3", 9600)

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

half_width = (width/2)
half_height = (height/2)

detector = cv2.CascadeClassifier(r"C:\Users\JP\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

while True:
    success, frame = cap.read()
    faces = detector.detectMultiScale(frame)

    largest_area = 0
    largest_face = None

    for face in faces:
        x, y, w, h = face
        area = w*h
        if area > largest_area:
            largest_area = area
            largest_face = face

    if len(faces) > 0:
        x, y, w, h = largest_face

        center_x = x + (w/2)
        center_y = y + (h/2)

        error_x = (center_x - half_width) * 100     / half_width
        error_y = (center_y - half_height) * 100 / half_height
        
        cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0, 0, 255), 1)
        cv2.circle(frame, (int(center_x), int(center_y)), 10, (0, 255, 0), 1)
        cv2.circle(frame, (int(half_width), int(half_height)), 10, (255, 0, 0), 1)

        print(error_x, error_y)

        data = (f"{error_x}, {error_y}\n")
        bytes_data = data.encode()
        arduino.write(bytes_data)
    
    cv2.imshow("window", frame)
    cv2.waitKey(2)