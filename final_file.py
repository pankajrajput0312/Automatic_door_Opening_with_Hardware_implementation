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
import datetime
from sms_send import send_sms
import move_stepper


def function():
    door_opening_time = 0
    # load our serialized face detector model from disk
    prototxtPath = r"./face_detector/deploy.prototxt"
    weightsPath = r"./face_detector/res10_300x300_ssd_iter_140000.caffemodel"
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("trained_model.yml")
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
    print("[INFO] starting video stream...")

    vs = VideoStream(src=0).start()
    time = None
    check = False
    starting_time = datetime.datetime.now()
    door_open = False
    unknown_visit = False
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=600)

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
            curr_time = datetime.datetime.now()

            time_delta = (curr_time - starting_time)
            total_seconds = time_delta.total_seconds()
            if(confidence < 70):
                if(check == False and total_seconds > 5):
                    print(total_seconds)
                    check = True
                    door_opening_time = datetime.datetime.now()

                    send_sms(9315630275, Id)

                    from get_details import details
                    move_stepper.stepper_move(90)
                    person_details = list(details(Id))
                    door_open = True

                    print("Welcome to our House....")
                    print("door opens for Next 20 seconds "+str(person_details[1])+" unique_id "+str(
                        person_details[0])+" Email_id: "+str(person_details[2]))
                elif(check == True and door_open == True):
                    door_opening_differnce = curr_time - door_opening_time
                    seconds = door_opening_differnce.total_seconds()
                    if(seconds > 20):
                        move_stepper.stepper_move(90)
                        door_open = False
                        print("Now Door Closing, Thank you for coming")
                # print(Id, confidence)

                label = "{}".format(str(Id))

                # display the label and bounding box rectangle on the output
                # frame
                color = (255, 255, 0)
                cv2.putText(frame, label, (startX, startY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            else:
                label = "unknown"
                if(unknown_visit == False):
                    print("Door doesn't open because you are not in database.")
                    send_sms(9810904773, 0)
                    unknown_visit = True
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
