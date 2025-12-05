from mpu6050 import mpu6050
sensor = mpu6050(0x68)
while True:
	print(mpu6050.get_gyro_data())
