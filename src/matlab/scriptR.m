% Auto-generated by cameraCalibrator app on 07-Jun-2016
%-------------------------------------------------------


% Define images to process
imageFileNames = {'/home/kaksoispiste/Code/calibpy/src/img/right1.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right10.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right11.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right2.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right3.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right4.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right5.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right6.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right7.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right8.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right9.png',...
    };

% Detect checkerboards in images
[imagePoints, boardSize, imagesUsed] = detectCheckerboardPoints(imageFileNames);
imageFileNames = imageFileNames(imagesUsed);

% Generate world coordinates of the corners of the squares
squareSize = 30;  % in units of 'mm'
worldPoints = generateCheckerboardPoints(boardSize, squareSize);

% Calibrate the camera
[cameraParamsR, imagesUsed, estimationErrors] = estimateCameraParameters(imagePoints, worldPoints, ...
    'EstimateSkew', false, 'EstimateTangentialDistortion', false, ...
    'NumRadialDistortionCoefficients', 2, 'WorldUnits', 'mm');

% View reprojection errors
h1=figure; showReprojectionErrors(cameraParamsR, 'BarGraph');

% Visualize pattern locations
h2=figure; showExtrinsics(cameraParamsR, 'CameraCentric');

% Display parameter estimation errors
displayErrors(estimationErrors, cameraParamsR);

% For example, you can use the calibration data to remove effects of lens distortion.
originalImage = imread(imageFileNames{1});
undistortedImage = undistortImage(originalImage, cameraParamsR);

% See additional examples of how to use the calibration data.  At the prompt type:
% showdemo('MeasuringPlanarObjectsExample')
% showdemo('SparseReconstructionExample')
