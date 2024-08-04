# Required imports
from collections import deque
import numpy as np
import cv2
import serial

#Create object for serial 
s=serial.Serial()

# Parameters class include important paths and constants
class Parameters:
    def __init__(self):
        self.CLASSES = open("model/action_recognition_kinetics.txt"
                            ).read().strip().split("\n")
        self.ACTION_RESNET = 'model/resnet-34_kinetics.onnx'
        self.SAMPLE_DURATION = 16
        self.SAMPLE_SIZE = 112

# Initialise instance of Class Parameter
param = Parameters()

# A Double ended queue to store our frames captured and with time
captures = deque(maxlen=param.SAMPLE_DURATION)

# load the human activity recognition model
print("[INFO] loading human activity recognition model...")
net = cv2.dnn.readNet(model=param.ACTION_RESNET)

print("[INFO] accessing video stream...")
# Take video file as input if given else turn on web-cam
vs = cv2.VideoCapture(0)

previous_label = None

while True:
    # Loop over and read capture from the given video input
    (grabbed, capture) = vs.read()

    # break when no frame is grabbed (or end if the video)
    if not grabbed:
        print("[INFO] no capture read from stream - exiting")
        break

    # resize frame and append it to our deque
    capture = cv2.resize(capture, dsize=(550, 400))
    captures.append(capture)

    # Process further only when the deque is filled
    if len(captures) < param.SAMPLE_DURATION:
        continue

    # now that our captures array is filled we can
    # construct our image blob
    imageBlob = cv2.dnn.blobFromImages(captures, 1.0,
                                       (param.SAMPLE_SIZE,
                                        param.SAMPLE_SIZE),
                                       (114.7748, 107.7354, 99.4750),
                                       swapRB=True, crop=True)

    imageBlob = np.transpose(imageBlob, (1, 0, 2, 3))
    imageBlob = np.expand_dims(imageBlob, axis=0)

    # Forward pass through model to make prediction
    net.setInput(imageBlob)
    outputs = net.forward()
    label = param.CLASSES[np.argmax(outputs)]
    label.lower()
    if label != previous_label:
        print(label)
        if label == "sleep reading":
            print(1)
        elif label == "watching tv":
            print(2)
        elif label == "relaxing":
            print(3)
        elif label=="sleeping":
            print(4)
        elif label=="reading":
            print(5)
        elif label=="texting":
            print(6)


        previous_label = label

    # Show the predicted activity
    cv2.rectangle(capture, (0, 0), (300, 40), (255, 255, 255), -1)
    cv2.putText(capture, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 0, 0), 2)

    # Display it on the screen
    cv2.imshow("Human Activity Recognition", capture)

    key = cv2.waitKey(1) & 0xFF
    # Press key 'q' to break the loop
    if key == ord("q"):
        break

vs.release()
#s.close()
cv2.destroyAllWindows()