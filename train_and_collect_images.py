import matplotlib.pyplot as plt
import os
import cv2
import shutil


def detect_faces(frame, faceNet, Id, count):
    # grab the dimensions of the frame and then construct a blob

    from tensorflow.keras.preprocessing.image import img_to_array
    from imutils.video import VideoStream
    import numpy as np
    import imutils
    import time
    import cv2
    import os
    (h, w) = frame.shape[:2]

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
                                 (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the face detections
    faceNet.setInput(blob)
    detections = faceNet.forward()
    # print(detections.shape)

    # initialize our list of faces, their corresponding locations,
    # and the list of predictions from our face mask network
    faces = []
    locs = []
    preds = []

    # loop over the detections

    # print(frame.shape)

    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the detection
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the confidence is
        # greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for
            # the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # ensure the bounding boxes fall within the dimensions of
            # the frame
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            # extract the face ROI, convert it from BGR to RGB channel
            # ordering, resize it to 224x224, and preprocess it
            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)

            img_name_path = Id + '.' + str(count) + ".jpg"

            # plt.imsave(img_name_path, face, cmap='gray')
            status = cv2.imwrite(img_name_path, face)
            dest = './data_images'
            try:
                shutil.move(img_name_path, dest)
            except Exception as e:
                print(e)
            # add the face and bounding boxes to their respective
            # lists
            faces.append(face)
            locs.append((startX, startY, endX, endY))
    faces = np.array(faces, dtype="float32")
    # only make a predictions if at least one face was detected

    return locs


def collect_data(faceNet):
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import cv2
    from PIL import Image
    import PIL
    import os
    import shutil
    import datetime
    import time
    from threading import Thread
    cap = cv2.VideoCapture(0)
    # face_cascade = cv2.CascadeClassifier(
    #     './haarcascade_frontalface_default.xml')

    name = input("enter name of person")
    Id = input(" enter unique id (aadhar card) ")
    Email_id = input("enter Email_id ")
    Phone_no = input("enter your phone number: ")
    from add_details_incsv import add_details
    # order add_details(Name,unique_id,email_id,phone_no)
    add_details(str(name), str(Id), str(Email_id), str(Phone_no))
    img_count = 0
    while(True):
        ret, frame = cap.read()
        if(ret == False):
            continue
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        faces = detect_faces(frame, faceNet, Id, img_count)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (w, h), (51, 255, 51), 3)
            img_count += 1

            img_name_path = Id + '.' + str(img_count) + ".jpg"
            offset = 10
            if(img_count % 50 == 0):
                print(img_name_path)
#             saving_image = gray[x:x+w, y:y+h]

#             plt.imsave(img_name_path, gray[y:y+h, x:x+w], cmap='gray')
#             status=cv2.imwrite(img_name_path, saving_image, [cv2.IMWRITE_JPEG_QUALITY, 100])
#             dest = './data_images'
#             shutil.move(img_name_path, dest)

        cv2.imshow("frame", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif(img_count > 150):
            break

    cap.release()
    cv2.destroyAllWindows()


def capture_data_details():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import cv2
    from PIL import Image
    import PIL
    import os
    import shutil
    import datetime
    import time
    from threading import Thread
    faces = []
    Ids = []
    for one in os.listdir('./data_images'):
        new_path = os.path.join('data_images', one)
        img = Image.open(new_path).convert('L')
        img = np.array(img, 'uint8')
        curr_id = int(one.split('.')[0])
        print(curr_id)
        Ids.append(curr_id)
        faces.append(img)
    return faces, Ids


def train_data():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import cv2
    from PIL import Image
    import PIL
    import os
    import shutil
    import datetime
    import time
    from threading import Thread
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    face, Ids = capture_data_details()
    recognizer.train(face, np.array(Ids))
    try:
        recognizer.save("trained_model.yml")
        print("model trained successfully!")
    except:
        print("unable to train model")


def add_new_person():
    import cv2
    prototxtPath = r"./face_detector/deploy.prototxt"
    weightsPath = r"./face_detector/res10_300x300_ssd_iter_140000.caffemodel"
    # prototxtPath = r"face_detector\deploy.prototxt"
    # weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
    # collect_data(faceNet)
    print("collect data successfullt")
    print("model training start...")
    train_data()
    print("New person added successfully...")


add_new_person()
