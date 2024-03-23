import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap=cv2.VideoCapture(0)
detector=FaceDetector();

arduino =SerialObject("COM3")


while True:
    success, img=cap.read()
    img, bbboxs= detector.findFaces(img)
    if bbboxs:
        arduino.sendData([1])
    else :
        arduino.sendData([0])

    cv2.imshow("Image",img)
    cv2.waitKey(1)