#!/bin/bash

#This script extracts plant attributes from an image
#Invoke this via cron on a regular (hourly?) basis to refresh the data
#Author: Howard Webb
#Date: 11/5/2017

echo "Process image for plant data"

#Modify this path if you move the webcam image directory
pic_dir="/home/pi/MVP/pictures/"
pic2_dir="/home/pi/MVP/pictures_R/"
web_dir="/home/pi/MVP/web/"
python_dir="/home/pi/python/"

#Pipe ls of the webcam directory from most recent to latest
# Then clip off only the last line
# Finally trim the string to just the name and store in the variable (File Name)
FN=$(ls -latr "$pic2_dir" | tail -1 | awk '{print $NF}')

#Check that got what expected
echo "$pic_dir$FN"

#Finally process the file
python "$python_dir"findSeedling.py $pic2_dir$FN
