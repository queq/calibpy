#include <opencv2/opencv.hpp>
#include <opencv/highgui.h>
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
	Mat frame, frame2, stereo;							// Create Matrix to store image
	VideoCapture cap(1), cap2(2);				// Initialize capture

	if (!(cap.isOpened() && cap2.isOpened()))				// Check if we succeeded
		return -1;

	namedWindow("Left", 1);			// Create window to show image
  namedWindow("Right", 1);

	while (1) {
		cap >> frame;					// Copy webcam stream to image
    cap2 >> frame2;

		imshow("Left", frame);			// Print image to screen
    imshow("Right", frame2);

		if (waitKey(1) == 27) break;	// Delay 1ms, break if Esc key is pressed
	}
	return 0;
}
