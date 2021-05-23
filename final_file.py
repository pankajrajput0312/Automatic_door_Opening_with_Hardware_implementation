import get_face
from tensorflow.keras.preprocessing.image import img_to_array
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os
import pandas as pd
import face_recognize2


def function():

    # load our serialized face detector model from disk
    prototxtPath = r"./face_detector/deploy.prototxt"
    weightsPath = r"./face_detector/res10_300x300_ssd_iter_140000.caffemodel"
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("trained_model.yml")
    # prototxtPath = r"face_detector\deploy.prototxt"
    # weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time = None
    check = False
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        # detect faces in the frame and determine if they are wearing a
        # face mask or not
        # (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)
        locs = get_face.detect_faces(frame, faceNet)

        # loop over the detected face locations and their corresponding
        # locations
        for box in locs:
            # unpack the bounding box and predictions
            (startX, startY, endX, endY) = box
            image = frame[startY:endY, startX:endX]
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # cv2.imshow("short",image)
            # determine the class label and color we'll use to draw
            # the bounding box and text
            Id, confidence = face_recognize2.testing(image, recognizer)

            if(check == False):
                check = True

                from sms_send import send_sms

                send_sms(9315630275, Id)
            print(Id, confidence)

            label = "{}".format(str(Id))

            # display the label and bounding box rectangle on the output
            # frame
            color = (255, 255, 0)
            cv2.putText(frame, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

        # show the output frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

# do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()


function()
