# ESP32-CYD-Menu-Script
A small part of a bigger project i'm working on, this is a interactive menu built to be expanded on. To be installed on a esp32-cyd TFT display (touchscreen))


Refer to the cheetsheet / driver to see how the developer of the driver (not me) has made functions work and what arguments they take.


NOTE: THIS IS A MICROPYTHON PROJECT, INSTALL LATEST VERSION ( my current is 1.26.0 )


files to load onto board:
/lib (all files + folder)
/main.py
/init.py

you may need to build a boot.py to launch the main.py or rename the main.py to boot.py so micropython knows to run it on startup

Expected Output

![IMG_6086](https://github.com/user-attachments/assets/943311c8-90b7-4518-aaf2-6c40d3783f25)
