#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an analog sensor connected to PORT_1 of the BrickPi3
# 
# Hardware: Connect an analog sensor (such as an NXT touch, light, or sound sensor) to sensor port 1 of the BrickPi3.
# 
# Results:  When you run this program, you will see the raw sensor value as well as the sensor voltage.

import time     # import the time library for the sleep function
from Software.Python.brickpi3 import *
 # import the BrickPi3 drivers

BP = BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.CUSTOM, [(BP.SENSOR_CUSTOM.PIN1_ADC)]) # Configure for an analog on sensor port pin 1, and poll the analog line on pin 1.

try:
    while True:
        # read the sensor value
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns a list of 4 values.
        #     The first is the pin 1 analog line value (what we want to display).
        #     The second is the pin 6 analog line value.
        #     The third is the pin 5 digital value.
        #     The fourth is the pin 6 digital value.
        try:
            value = BP.get_sensor(BP.PORT_1)[0] # read the sensor port value
            print("Raw value: %4d   Voltage: %5.3fv" % (value, (value / (4095.0 / BP.get_voltage_5v())))) # print the raw value, and calculate and print the voltage as well
        except SensorError as error:
            print(error)
        
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
