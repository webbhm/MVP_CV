#!/bin/sh

RED='\033[31;47m'
NC='\033[0m'

# Exit on error
error_exit()
{
	echo ${RED} $(date +"%D %T") "${PROGNAME}: ${1:="Unknown Error"}" ${NC} 1>&2
	exit 1
}

# Update what have
sudo apt-get update

# Build directories
mkdir /home/pi/MVP || error_exit "Failure to build MVP directory"
cd /home/pi/MVP
mkdir data
mkdir logs
mkdir pictures
ECHO $(date -u) "directories created"

#Create variables
# Build the environment information

python /home/pi/MVP/python/buildEnv.py || error_exit "Failure to build environment variables"
ECHO  $(date +"%D %T") "Environment variables built"


# FS Webcam
sudo apt-get updatesudo apt-get install fswebcam  || error_exit "Failure to install fswebcam (USB Camera support)"
ECHO  $(date +"%D %T") "fswebcam intalled (supports USB camera"

# Used for charting
sudo pip install pygal || error_exit "Failure to install pygal (needed for charting)"
ECHO  $(date +"%D %T") "pygal installed (used for charting)"

# CouchDB python library
# http://pythonhosted.org/CouchDB

pip install  pycouchdb || error_exit "Failure to install CouchDB Python library"
ECHO  $(date +"%D %T") "CouchDB Python Library intalled"

# OpenCV library
# https://www.raspberrypi.org/forums/viewtopic.php?t=142700
# numpy dependency

sudo apt-get install python-numpy || error_exit "Failure to install numpy math library"
ECHO  $(date +"%D %T") "numpy Library intalled"

sudo apt-get install python-scipy
ECHO  $(date +"%D %T") "scipy Library intalled"

sudo apt-get install ipython || error_exit "Failure to install ipython library"
ECHO  $(date +"%D %T") "ipython Library intalled"

sudp apt-get install libopencv-dev python-opencv || error_exit "Failure to install opencv (computer vision) library"
ECHO  $(date +"%D %T") "opencv Library intalled"

# Make scripts executable
ECHO $(date +"%D %T") "Scripts set to executable"

# Test System


sudo bash /home/pi/MVP/scripts/render.sh
ECHO $(date +"%D %T") "System PASSED"

# Load Cron

ECHO $(date +"%D %T") "Your MVP is now running"
reboot