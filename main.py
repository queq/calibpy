import calib
import cv2

grid = (7, 6)
stereo = calib.createStereoPair(0, 1)
iobjp = calib.createChessboard(grid, 3)
objp = []
imgp = [[], []]

while True:
    frames = calib.captureFromStereo(stereo)
    frames, objp, imgp = calib.findChessboardCorners(frames, grid, iobjp, objp, imgp)
    frame = calib.combineStereoFrames(frames, swap=True)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
calib.releaseStereoPair(stereo)
cv2.destroyAllWindows()
