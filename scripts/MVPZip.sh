#!/bin/sh

# Exit on error
error_exit()
{
	echo $(date +"%D %T") "${PROGNAME}: ${1:="Unknown Error"}" 1>&2
	exit 1
}

BLD_DIR=/home/pi/

# Download MVP fro GitHub and install
# Build directory
mkdir /home/pi/junk || error_exit "Failure to build working directory"
ECHO $(date +"%D %T") "Directory built"
cd /home/pi/junk

#Download for Github
curl -Lok https://github.com/webbhm/OpenAg_MVP_UI/archive/master.zip > mvp_ui.zip || error_exit "Failure to download zip file"
ECHO $(date +"%D %T") "OpenAg_MVP Github downloaded"

# Unzip the files
unzip /home/pi/junk/mvp_ui.zip || error_exit "Failure unzipping file"
ECHO $(date +"%D %T") "OpenAg_MVP unzipped"

# Remove the zip file
rm /home/pi/junk/mvp_ui.zip || error_exit "Failure unzipping file"
ECHO $(date +"%D %T") "zip file deleted"
