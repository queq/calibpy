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

i = 1

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # stereo = np.concatenate((frame,frame2), axis=1)

    # Display the resulting frame
    cv2.imshow('Left', frame)
    cv2.imshow('Right', frame2)
    # cv2.imshow('Stereo', stereo)

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('left{}.png'.format(i), frame)
        cv2.imwrite('right{}.png'.format(i), frame2)
        i += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
