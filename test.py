# import time as t
#
# start = t.time()
#
# TIME = 10
# count = 0
#
# while True:
#     interval = t.time() - start
#     if interval == 1.0:
#         if count < TIME - 1:
#             print "Time!"
#             count += 1
#             start = t.time()
#         else:
#             print "Time is over!"
#             break


import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    stereo = np.concatenate((gray,gray2), axis=1)

    # Display the resulting frame
    cv2.imshow('frame', stereo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
