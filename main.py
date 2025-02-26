import cv2
import numpy
import time
from Mailing import send_email

# Access laptop webcam
video=cv2.VideoCapture(0)
time.sleep(1)
first_frame=None

while True:
    check, frame = video.read()
    grey_frame=cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
    grey_frame_gb=cv2.GaussianBlur(grey_frame,(21,21),0)


    if first_frame is None :
        first_frame = grey_frame_gb

    delta_frame = cv2.absdiff(first_frame,grey_frame_gb)

    thresh_frame=cv2.threshold(delta_frame,50,225,cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame,None,iterations=2)
    cv2.imshow("video", dil_frame)

    contors, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contor in contors:
        if cv2.contourArea(contor) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contor)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if rectangle.any():
            send_email()

    cv2.imshow("Updated_video",frame)



    key=cv2.waitKey(1)

    # Add a key to break the loop and end the video
    if key==ord('q'):
        break


video.release()



