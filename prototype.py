#!/usr/bin/env python3
from mpu6050 import mpu6050
sensor = mpu6050(0x68)
while True:
	print(sensor.get_gyro_data())
