
def testing(frame, recognizer):
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy
    import cv2
    from PIL import Image
    import PIL
    import os
    import shutil
    frame = numpy.array(frame)
    # cv2.imshow("gray",frame)
    Id, confidence = recognizer.predict(frame)
    return Id, confidence
