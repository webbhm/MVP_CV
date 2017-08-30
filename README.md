# MVP_CV
This is a collection of OpenCV Python code I have experimented with to identify plants in the MVP.
The code is 'rough', as it is experimental; changes for a different file, or prameters have to be done in the code (this is not command line parameters).
### Setup
  - copy the code to a working directory
  - install [OpenCV](http://opencv.org/).  The Python 2.7 and 3.0 versions are different (parameter and coding style changes - not mutually compatable).
>> sudo apt-get install libopencv-dev python-opencv
The tutorials are very helpful and worth the time to work through, or at least copy the code and see what they do.
### Description of Programs
  - OpenCV_PickPoint.py: a helper program that tells you the point coordinates of the mouse location.  I use this for the warping function parameters.  It is helpful to hold a piece of paper against the screen to extend the edge of the reservoir to the top of the image, so as to find the pixel in the top (or bottom) row.  If you set the output points to the left edge of the image ([0,0][0,270]) and the right side to be the top and bottom of the max width, you should have it working.
  - GreenParms.py: This is a fun one to play with; there are sliders for adjusting the lower (darker) and upper (lighter) bounds of the colors you want to pick from the image, and it dynamically shows you the edges and ellipse that would be formed.  You can copy the output in the IDE to your code for the upper and lower parameters of the getMask function.
  - findPlantUtil.py: the core functionality, called by most of the other programs.  It is a collection of functions to Warp images (straighten the tub and remove side walls. Mask: detect an area of color and turn it into a black & white 'mask' for further processing.  getEdges: finds the edges of the mask (or other image).  getContours: builds a collection of line segments from the edges image.
  - findPlant_1.py: takes a single image and goes through the steps to create an image with the plant circled by an ellipse.
  - findPlant_2.py: similar to findPlant_1.py, but has the warp process commented out.
  - findPlant_batch.py: walks through a directory of images and outputs them as a batch of processed images.
  - img2video.py: takes the processed images (or any images) and turns them into a video.
### Comments
You are on your own with the code.  There is no support and no guarantees, but it is something that may help to get you started.
An interesting note.  [OpenAg](https://github.com/OpenAgInitiative/openag_cv) uses the same basic code, but follows a different processing path.  Instead of looking for colors, they go directly to edge detection.  This has some advantages, but requires a 'clean' box with no extraneous artifacts in the picture.  They have some additional libraries, but do some interesting stuff with drawing boxes around the plants and calculating some information.
