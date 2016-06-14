% Auto-generated by stereoCalibrator app on 09-Jun-2016
%-------------------------------------------------------


% Define images to process
imageFileNames1 = {'/home/kaksoispiste/Code/calibpy/src/img/left/left10.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left11.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left13.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left14.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left16.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left17.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left19.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left20.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left21.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left4.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left5.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left6.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left7.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left8.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/left/left9.png',...
    };
imageFileNames2 = {'/home/kaksoispiste/Code/calibpy/src/img/right/right10.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right11.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right13.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right14.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right16.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right17.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right19.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right20.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right21.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right4.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right5.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right6.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right7.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right8.png',...
    '/home/kaksoispiste/Code/calibpy/src/img/right/right9.png',...
    };

% Detect checkerboards in images
[imagePoints, boardSize, imagesUsed] = detectCheckerboardPoints(imageFileNames1, imageFileNames2);

% Generate world coordinates of the checkerboard keypoints
squareSize = 30;  % in units of 'mm'
worldPoints = generateCheckerboardPoints(boardSize, squareSize);

% Calibrate the camera
[stereoParams, pairsUsed, estimationErrors] = estimateCameraParameters(imagePoints, worldPoints, ...
    'EstimateSkew', false, 'EstimateTangentialDistortion', false, ...
    'NumRadialDistortionCoefficients', 2, 'WorldUnits', 'mm', ...
    'InitialIntrinsicMatrix', [], 'InitialRadialDistortion', []);

% View reprojection errors
h1=figure; showReprojectionErrors(stereoParams, 'BarGraph');

% Visualize pattern locations
h2=figure; showExtrinsics(stereoParams, 'CameraCentric');

% Display parameter estimation errors
displayErrors(estimationErrors, stereoParams);

% You can use the calibration data to rectify stereo images.
I1 = imread(imageFileNames1{1});
I2 = imread(imageFileNames2{1});
[J1, J2] = rectifyStereoImages(I1, I2, stereoParams);

% See additional examples of how to use the calibration data.  At the prompt type:
% showdemo('StereoCalibrationAndSceneReconstructionExample')
% showdemo('DepthEstimationFromStereoVideoExample')
