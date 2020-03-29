# BeetleBloatware
Beetle EV Auxilary Control System.

Written in Python 3.7
GUI written using Kivy 1.11.1

Description:
The general goal of the Beetle EV Conversion project is to restore an old Wolkswagon Beetle and convert the restored car
to an EV. The purpose of the Auxilary Control System is to interface between a touchscreen (to be specified later) and 
Rasberry Pi (RPi). The Rasberry Pi will act as the main system to control auxilary functions of the car (i.e. headlights,
taillights, windshield wipers, windows, etc.). 

GPIO Pins !!! IN USE !!!
Headlights -- 17
Brights -- 27

constants.py
Holds the constant values for all variables in a nice convienent location

Lights (external)
The Lights directory contains only one Python script (sad). It contorls the headlights and the brights. The widget is
structured with a chold boxlayout that contains two buttons in a vertical orientation.
