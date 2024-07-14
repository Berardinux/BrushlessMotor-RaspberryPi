from gpiozero import PWMOutputDevice
import time

PIN = 26

motor = PWMOutputDevice(PIN, frequency=50)

print("Full throttle")
motor.value = .1
time.sleep(2)

print("Low Speed")
motor.value = .05
time.sleep(2)

print("Half Speed")
motor.value = .075
time.sleep(4)

motor.value = 0

print("GPIO cleaned up.")