import calib
import cv2
import time

grid = (7, 6)
stereo = calib.createStereoPair(1, 2)
iobjp = calib.createChessboard(grid, 3)
objp = []
imgp = [[], []]
countdown = calib.FRAME_INTERVAL
n = 0
delta = 0.2
t0 = time.time()

while True:
    frames = calib.captureFromStereo(stereo)
    interval = time.time() - t0
    print interval
    if interval > (1.0 - delta) and interval < (1.0 + delta):
        print "Interval {}".format(countdown)
        t0 = time.time()
        if countdown > 0:
            countdown -= 1

    if interval > (1.0 + delta):
        t0 = time.time()

    append = True if countdown == 0 else False

    frames, n, objp, imgp = calib.findChessboardCorners(frames, n, grid, iobjp, objp, imgp, append)

    if append is True:
        countdown = calib.FRAME_INTERVAL
        append = False
        if n == calib.MAX_FRAMES:
            # Calibrate
            break

    frame = calib.combineStereoFrames(frames, swap=True)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
calib.releaseStereoPair(stereo)
cv2.destroyAllWindows()
