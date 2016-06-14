#include <opencv2/opencv.hpp>
#include <opencv/highgui.h>
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
	Mat image;							// Create Matrix to store image
	VideoCapture cap(1);				// Initialize capture
	if (!cap.isOpened())				// Check if we succeeded
		return -1;

	namedWindow("Frame", 1);			// Create window to show image
	while (1) {
		cap >> image;					// Copy webcam stream to image
		imshow("Frame", image);			// Print image to screen
		if (waitKey(1) == 27) break;	// Delay 1ms, break if Esc key is pressed 
	}
	return 0;
}